import numpy as np
import joblib
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import (
    UserSerializer, RegisterSerializer, ProfileUpdateSerializer,
    PredictionInputSerializer, PredictionSerializer, ResumeUploadSerializer
)
from .models import Profile, UserPredictModel1, ResumeUpload
from .resume_processor import analyze_resume
from Chatbot.processor import chatbot_response

# Load ML model once at module level
try:
    ml_model = joblib.load('users/placement_new2.pkl')
except Exception:
    ml_model = None


# ---------- Auth Endpoints ----------

@api_view(['POST'])
@permission_classes([AllowAny])
def api_register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': UserSerializer(user).data,
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def api_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Username and password are required.'},
                        status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request, username=username, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': UserSerializer(user).data,
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        })
    return Response({'error': 'Invalid credentials.'},
                    status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_logout(request):
    try:
        refresh_token = request.data.get('refresh')
        if refresh_token:
            token = RefreshToken(refresh_token)
            token.blacklist()
        return Response({'message': 'Logged out successfully.'})
    except Exception:
        return Response({'message': 'Logged out.'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_user(request):
    return Response(UserSerializer(request.user).data)


# ---------- Profile Endpoints ----------

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser, JSONParser])
def api_profile(request):
    if request.method == 'GET':
        return Response(UserSerializer(request.user).data)

    serializer = ProfileUpdateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.update(request.user, serializer.validated_data)
        return Response(UserSerializer(request.user).data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ---------- Prediction Endpoints ----------

def _calculate_academic_score(cgpa, ten_percentage, twelth_percentage):
    cgpa_score = (float(cgpa) / 10) * 40
    ten_score = (float(ten_percentage) / 100) * 30
    twelth_score = (float(twelth_percentage) / 100) * 30
    return round(cgpa_score + ten_score + twelth_score)


def _calculate_skill_score(job_role, soft_skills):
    base_score = 60
    job_role_bonus = int(job_role) * 2
    soft_skills_bonus = int(soft_skills) * 3
    return min(base_score + job_role_bonus + soft_skills_bonus, 100)


def _calculate_experience_score(internship, experience, rounds):
    score = 50
    if int(internship) == 1:
        score += 20
    if int(experience) == 1:
        score += 20
    score += min(int(rounds) * 3, 10)
    return min(score, 100)


def _calculate_company_fit(company_name, qualification):
    base_fit = 70
    company_bonus = int(company_name) % 30
    qualification_bonus = int(qualification) * 2
    return min(base_fit + company_bonus + qualification_bonus, 100)


def _generate_recommendations(prediction, data):
    """Use Gemini to generate personalized recommendations"""
    try:
        import google.generativeai as genai
        GEMINI_API_KEY = "AIzaSyAm_LJ6O0mmZrC_KaHuu26HuspW_PSUZDY"
        genai.configure(api_key=GEMINI_API_KEY)
        gemini_model = genai.GenerativeModel("gemini-2.5-flash")

        prompt = f"""
        You are an expert career advisor.

        Student Details:
        - Age: {data['Age']}
        - Gender: {data['Gender']}
        - Qualification: {data['Qualification']}
        - Year of Study: {data['year']}
        - CGPA: {data['cgpa']}
        - Job Role: {data['Job_Role']}
        - Post Graduation: {data['Post_Graduation']}
        - 10th Percentage: {data['ten_Percentage']}
        - 12th Percentage: {data['twelth_Percentage']}
        - Expected Salary: {data['Salary']}
        - Soft Skills Score: {data['Soft_Skills']}
        - Internship Count: {data['Internship']}
        - Experience (years): {data['Experience']}
        - Interview Round Cleared: {data['Round']}
        - Company Name: {data['Company_Name']}

        Placement Prediction Result: {prediction}

        Instructions:
        - Generate 5 short, actionable, personalized recommendations.
        - Each should be one sentence.
        - Focus on weak areas and career improvement.
        - Do not use numbering or bullet characters in the text.
        """

        response = gemini_model.generate_content(prompt)
        text = response.text.strip()
        recommendations = [line.strip("-• ").strip()
                           for line in text.split("\n") if line.strip()]
        return recommendations[:5]
    except Exception as e:
        print("Gemini Error:", e)
        return [
            "Focus on improving your technical skills",
            "Work on practical real-world projects",
            "Strengthen your communication skills",
            "Prepare consistently for interviews",
            "Build a strong professional network"
        ]


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_predict(request):
    serializer = PredictionInputSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    data = serializer.validated_data

    if ml_model is None:
        return Response({'error': 'Model not loaded.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Build feature array
    feature = np.array([[
        data['Age'], data['Gender'], data['Qualification'], data['year'],
        data['cgpa'], data['Job_Role'], data['Post_Graduation'],
        data['ten_Percentage'], data['twelth_Percentage'], data['Salary'],
        data['Soft_Skills'], data['Internship'], data['Experience'],
        data['Round'], data['Company_Name']
    ]])

    predictions = ml_model.predict(feature)
    result = predictions[0]
    prediction_result = 'yes' if result == 1 else 'NO'

    try:
        probability = ml_model.predict_proba(feature)[0][1] * 100
    except Exception:
        probability = 85 if prediction_result == 'yes' else 35

    # Save to database
    UserPredictModel1.objects.create(
        user=request.user,
        Age=data['Age'],
        Gender=data['Gender'],
        Qualification=data['Qualification'],
        year=data['year'],
        cgpa=data['cgpa'],
        Job_Role=data['Job_Role'],
        Post_Graduation=data['Post_Graduation'],
        ten_Percentage=data['ten_Percentage'],
        twelth_Percentage=data['twelth_Percentage'],
        Salary=data['Salary'],
        Soft_Skills=data['Soft_Skills'],
        Internship=data['Internship'],
        Experience=data['Experience'],
        Round=data['Round'],
        Company_Name=data['Company_Name'],
        label=prediction_result
    )

    # Calculate breakdown scores
    breakdown = {
        'academic_score': _calculate_academic_score(data['cgpa'], data['ten_Percentage'], data['twelth_Percentage']),
        'skill_score': _calculate_skill_score(data['Job_Role'], data['Soft_Skills']),
        'experience_score': _calculate_experience_score(data['Internship'], data['Experience'], data['Round']),
        'company_fit': _calculate_company_fit(data['Company_Name'], data['Qualification']),
        'overall_fit': min(probability * 1.1, 100),
    }

    recommendations = _generate_recommendations(prediction_result, data)

    return Response({
        'prediction': prediction_result,
        'probability': round(probability, 1),
        'form_data': data,
        'prediction_breakdown': breakdown,
        'recommendations': recommendations,
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_predictions(request):
    predictions = UserPredictModel1.objects.filter(user=request.user).order_by('-created_at')
    serializer = PredictionSerializer(predictions, many=True)
    return Response(serializer.data)


# ---------- Resume Endpoints ----------

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def api_resume_upload(request):
    serializer = ResumeUploadSerializer(data=request.data)
    if serializer.is_valid():
        instance = serializer.save(user=request.user)

        # Process the resume
        result = analyze_resume(
            file_field=instance.file,
            desired_roles=instance.job_role,
            job_keywords=None
        )

        instance.ats_score = result["ats_score"]
        instance.gemini_response = result["gemini_raw"]
        instance.suggestions = "\n".join(result.get("suggestions", []))
        instance.course_products = result.get("course_recommendations", [])
        instance.alternative_roles = result.get("recommended_roles", [])
        instance.role_courses = result.get("role_courses", [])
        instance.processed = True
        instance.save()

        return Response(ResumeUploadSerializer(instance).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_resume_result(request, pk):
    try:
        obj = ResumeUpload.objects.get(pk=pk, user=request.user)
    except ResumeUpload.DoesNotExist:
        return Response({'error': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

    gemini = obj.gemini_response or {}

    return Response({
        'resume': ResumeUploadSerializer(obj).data,
        'ats_score': obj.ats_score,
        'suggestions': obj.suggestions.splitlines() if obj.suggestions else [],
        'gemini': gemini,
        'course_recommendations': obj.course_products if obj.course_products else [],
        'roles': obj.alternative_roles if obj.alternative_roles else [],
        'role_courses': obj.role_courses if obj.role_courses else [],
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_resumes(request):
    resumes = ResumeUpload.objects.filter(user=request.user).order_by('-uploaded_at')
    serializer = ResumeUploadSerializer(resumes, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def api_resume_delete(request, pk):
    try:
        resume = ResumeUpload.objects.get(pk=pk, user=request.user)
    except ResumeUpload.DoesNotExist:
        return Response({'error': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

    resume.file.delete()
    resume.delete()
    return Response({'message': 'Resume deleted successfully.'})


# ---------- Chatbot Endpoint ----------

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_chatbot(request):
    question = request.data.get('question', '')
    if not question:
        return Response({'error': 'Question is required.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        response = chatbot_response(question)
        return Response({'response': response})
    except Exception as e:
        return Response({'response': 'Sorry, I could not process your request right now.'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout as auth_logout
import numpy as np
import joblib
from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm




def home(request):
    return render(request, 'users/home.html')

@login_required(login_url='users-register')


def index(request):
    return render(request, 'app/index.html')

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


# Class based view that extends from the built in login view to add a remember me functionality

class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})







from django.shortcuts import render
from django.http import JsonResponse
# import random
# import json
import numpy as np
# from nltk.tokenize import word_tokenize
# from nltk.stem import WordNetLemmatizer
#from .models import Response, models
from Chatbot.processor import chatbot_response
# Remove the comments to download additional nltk packages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@require_POST
@csrf_exempt
def chatbot_response_view(request):
    if request.method == 'POST':
        the_question = request.POST.get('question', '')

        response = chatbot_response(the_question)
        print(response)

        return JsonResponse({"response": response})
    else:
        
        return JsonResponse({"message": "This endpoint only accepts POST requests."})
 


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO
from django.shortcuts import render




def Report(request):
    return render(request,'app/Report.html')

from users.models import UserPredictModel1







def logout_view(request):  
    auth_logout(request)
    return redirect('/')




from django.shortcuts import render
import numpy as np

from django.contrib import messages

from django.views import View

import joblib


from .forms import Network_data_form


ml_model = joblib.load('users/placement_new2.pkl')

# views.py
from django.shortcuts import render
from .forms import Network_data_form
import numpy as np
import joblib
import json
from django.http import JsonResponse

# Load your model (adjust the path as needed)
ml_model = joblib.load('users/placement_new2.pkl')

def Model(request):
    form = Network_data_form()  
    
    if request.method == 'POST':
        form = Network_data_form(request.POST)
        
        if form.is_valid():
            cleaned_data = form.cleaned_data
            
            # Extract all fields
            Age = cleaned_data['Age']
            Gender = cleaned_data['Gender']
            Qualification = cleaned_data['Qualification']
            year = cleaned_data['year']
            cgpa = cleaned_data['cgpa']
            Job_Role = cleaned_data['Job_Role']
            Post_Graduation = cleaned_data['Post_Graduation']
            ten_Percentage = cleaned_data['ten_Percentage']
            twelth_Percentage = cleaned_data['twelth_Percentage']
            Salary = cleaned_data['Salary']
            Soft_Skills = cleaned_data['Soft_Skills']
            Internship = cleaned_data['Internship']
            Experience = cleaned_data['Experience']
            Round = cleaned_data['Round']
            Company_Name = cleaned_data['Company_Name']
            
            # Prepare feature array
            feature = np.array([[Age, Gender, Qualification, year, cgpa, Job_Role,
                                Post_Graduation, ten_Percentage, twelth_Percentage,
                                Salary, Soft_Skills, Internship, Experience, Round, Company_Name]])

            # Get prediction
            predictions = ml_model.predict(feature)
            result = predictions[0]

            if result == 0:
                prediction_result = 'NO'
            else:
                prediction_result = 'yes'

            # Calculate probability score (if your model supports it)
            try:
                probability = ml_model.predict_proba(feature)[0][1] * 100
            except:
                probability = 85 if prediction_result == 'yes' else 35

            # Save instance
            instance = form.save(commit=False)
            instance.user = request.user      # ✔ important line
            instance.label = prediction_result
            instance.save()
            
            # Prepare data for template
            context = {
                'predict': prediction_result,
                'probability': round(probability, 1),
                'form_data': cleaned_data,
                'prediction_breakdown': {
                    'academic_score': calculate_academic_score(cgpa, ten_Percentage, twelth_Percentage),
                    'skill_score': calculate_skill_score(Job_Role, Soft_Skills),
                    'experience_score': calculate_experience_score(Internship, Experience, Round),
                    'company_fit': calculate_company_fit(Company_Name, Qualification),
                    'overall_fit': calculate_overall_fit(probability)
                },
                'recommendations': generate_recommendations(prediction_result, cleaned_data)
            }
            
            return render(request, 'App/output.html', context)
    
    return render(request, 'app/Deploy_8.html', {'form': form})


def calculate_academic_score(cgpa, ten_percentage, twelth_percentage):
    """Calculate academic performance score"""
    cgpa_score = (float(cgpa) / 10) * 40
    ten_score = (float(ten_percentage) / 100) * 30
    twelth_score = (float(twelth_percentage) / 100) * 30
    return round(cgpa_score + ten_score + twelth_score)

def calculate_skill_score(job_role, soft_skills):
    """Calculate skill match score"""
    base_score = 60
    job_role_bonus = int(job_role) * 2  # Assuming job_role is encoded as integer
    soft_skills_bonus = int(soft_skills) * 3  # Assuming soft_skills is encoded as integer
    return min(base_score + job_role_bonus + soft_skills_bonus, 100)

def calculate_experience_score(internship, experience, rounds):
    """Calculate experience score"""
    score = 50
    if int(internship) == 1:
        score += 20
    if int(experience) == 1:
        score += 20
    score += min(int(rounds) * 3, 10)
    return min(score, 100)

def calculate_company_fit(company_name, qualification):
    """Calculate company fit score"""
    # This is a simplified version - you can implement more complex logic
    base_fit = 70
    company_bonus = int(company_name) % 30  # Simple scoring based on company
    qualification_bonus = int(qualification) * 2
    return min(base_fit + company_bonus + qualification_bonus, 100)

def calculate_overall_fit(probability):
    """Calculate overall fit score"""
    return min(probability * 1.1, 100)  # Slightly boost the probability





import google.generativeai as genai

# ✅ Replace with your real API key
GEMINI_API_KEY = "AIzaSyAm_LJ6O0mmZrC_KaHuu26HuspW_PSUZDY"

genai.configure(api_key=GEMINI_API_KEY)
gemini_model = genai.GenerativeModel("gemini-2.5-flash")




def generate_recommendations(prediction, data):
    """
    Use Gemini 2.5 Flash to generate personalized recommendations
    """

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

    try:
        response = gemini_model.generate_content(prompt)

        # Split response into clean list
        text = response.text.strip()
        recommendations = [line.strip("-• ").strip()
                           for line in text.split("\n") if line.strip()]

        return recommendations[:5]

    except Exception as e:
        print("Gemini Error:", e)
        # Fallback if API fails
        return [
            "Focus on improving your technical skills",
            "Work on practical real-world projects",
            "Strengthen your communication skills",
            "Prepare consistently for interviews",
            "Build a strong professional network"
        ]

def Database(request):
    data = UserPredictModel1.objects.filter(user=request.user)
    return render(request, 'app/Database.html', {'data': data})






from django.shortcuts import render, redirect, get_object_or_404
from .forms import ResumeUploadForm
from .models import ResumeUpload
from .resume_processor import analyze_resume


def upload_resume(request):
    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user    
            instance.save()

          
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

            return redirect('resume_result', pk=instance.pk)
    else:
        form = ResumeUploadForm()

    return render(request, 'app/upload_resume.html', {'form': form})


def resume_result(request, pk):
    obj = get_object_or_404(ResumeUpload, pk=pk, user=request.user)

    gemini = obj.gemini_response or {}

    context = {
        'resume': obj,
        'ats_score': obj.ats_score,
        'suggestions': obj.suggestions.splitlines() if obj.suggestions else [],
        'gemini': gemini,
        'course_recommendations': obj.course_products if obj.course_products else [],
        'roles': obj.alternative_roles if obj.alternative_roles else [],
        'role_courses': obj.role_courses if obj.role_courses else [],
    }

    return render(request, 'app/resume_result.html', context)


from django.shortcuts import render
from .models import ResumeUpload

from django.shortcuts import render, get_object_or_404, redirect
from .models import ResumeUpload
from django.contrib import messages


def resume_database(request):
    resumes = ResumeUpload.objects.filter(user=request.user).order_by('-uploaded_at')
    return render(request, 'app/resume_list.html', {'resumes': resumes})



def delete_resume(request, id):
    resume = get_object_or_404(ResumeUpload, id=id, user=request.user)
    resume.file.delete()
    resume.delete()
    messages.success(request, "Resume deleted successfully!")
    return redirect('resume_list')


import pdfplumber
from docx import Document
import re
import json
import google.genai as genai

# Configure your Gemini API
client = genai.Client(api_key="AIzaSyAVTzVDLsKZ4OZE2noZ4_2am6VVaiKyd8w")


# ---------- Helper functions ----------

def extract_text_from_pdf(file_obj):
    text = []
    with pdfplumber.open(file_obj) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text)
    return "\n".join(text)


def extract_text_from_docx(file_obj):
    doc = Document(file_obj)
    paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
    return "\n".join(paragraphs)


def extract_text(file_field):
    filename = file_field.name.lower()
    file_obj = file_field.file
    if filename.endswith('.pdf'):
        return extract_text_from_pdf(file_obj)
    elif filename.endswith('.docx') or filename.endswith('.doc'):
        return extract_text_from_docx(file_obj)
    else:
        try:
            txt = file_obj.read().decode('utf-8', errors='ignore')
        except Exception:
            file_obj.seek(0)
            txt = file_obj.read().decode('latin-1', errors='ignore')
        return txt


# ---------- ATS Score Function ----------

def compute_ats_score(text, job_keywords=None):
    words = re.findall(r'\w+', text.lower())
    word_count = len(words)

    has_contact = bool(re.search(r'\b(email|@|phone|linkedin|github)\b', text, re.I))
    has_skills = bool(re.search(r'\b(skills|technical skills|skills & tools)\b', text, re.I))
    has_experience = bool(re.search(r'\b(experience|work experience|professional experience)\b', text, re.I))
    has_education = bool(re.search(r'\b(education|bachelor|master|graduat)\b', text, re.I))

    length_score = 90 if 200 <= word_count <= 1000 else 75
    if word_count < 180:
        length_score = 60

    keyword_score = 80
    if job_keywords:
        found = sum(1 for k in job_keywords if k.lower() in text.lower())
        keyword_score = min(100, int(100 * found / max(1, len(job_keywords))))

    action_verbs = ['led', 'developed', 'built', 'improved', 'reduced', 'increased', 'designed', 'implemented']
    metrics_score = 90 if any(v in text.lower() for v in action_verbs) and bool(re.search(r'\b\d{1,3}%|\b\d{1,5}\b', text)) else 60

    grammar_score = 90

    score = (
        0.15 * (90 if has_contact else 50) +
        0.20 * length_score +
        0.20 * keyword_score +
        0.15 * metrics_score +
        0.15 * (90 if has_skills else 50) +
        0.15 * grammar_score
    )

    final = max(0, min(100, int(score)))

    breakdown = {
        "word_count": word_count,
        "has_contact": has_contact,
        "has_skills": has_skills,
        "has_experience": has_experience,
        "has_education": has_education,
        "length_score": length_score,
        "keyword_score": keyword_score,
        "metrics_score": metrics_score,
        "grammar_score": grammar_score,
    }

    return final, breakdown


# ---------- Gemini Analysis ----------

def call_gemini_analyze(resume_text, desired_roles=None):
    prompt = f"""
You are a career advisor + ATS expert. Analyze this resume and return JSON ONLY:
- ats_score: integer 0-100
- strengths: list of strings
- weaknesses: list of strings
- suggestions: list of strings
- course_recommendations: list of objects with 'title', 'provider', 'rating', 'url'
- recommended_roles: list of objects with 'role', 'description'
- role_courses: list of objects with 'course', 'topic', 'url'

Resume:
\"\"\"{resume_text[:4000]}\"\"\"

Job Role: {desired_roles if desired_roles else "N/A"}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    raw = getattr(response, "text", None) or str(response)

    try:
        start = raw.find("{")
        end = raw.rfind("}") + 1
        parsed = json.loads(raw[start:end])
    except Exception:
        parsed = {"raw_response": raw}

    return parsed


# ---------- Main Analyzer ----------

def analyze_resume(file_field, desired_roles=None, job_keywords=None):
    text = extract_text(file_field)

    # Call Gemini AI to get analysis
    gemini_result = call_gemini_analyze(text, desired_roles)

    # Heuristic ATS score
    ats_score, breakdown = compute_ats_score(text, job_keywords=job_keywords)
    gemini_ats = gemini_result.get("ats_score") if isinstance(gemini_result, dict) else None
    final_ats = int((ats_score + int(gemini_ats)) / 2) if gemini_ats else ats_score

    # ----------------------
    # Courses Recommendation Logic with Images
    # ----------------------
    courses = gemini_result.get("course_recommendations", [])

    # fallback courses based on desired_roles with images
    if not courses:
        role = desired_roles.lower() if desired_roles else ""
        if "data scientist" in role:
            courses = [
                {"title": "Advanced Machine Learning Specialization", "provider": "Coursera", "rating": 4.8,
                 "url":"https://www.coursera.org/specializations/aml",
                 "image_url":"https://d3njjcbhbojbot.cloudfront.net/api/utilities/v1/imageproxy/https://coursera-assets.s3.amazonaws.com/aml.jpg"},
                {"title": "Deep Learning Specialization", "provider": "Coursera", "rating": 4.7,
                 "url":"https://www.coursera.org/specializations/deep-learning",
                 "image_url":"https://d3njjcbhbojbot.cloudfront.net/api/utilities/v1/imageproxy/https://coursera-assets.s3.amazonaws.com/dl.jpg"},
                {"title": "Applied Data Science with Python", "provider": "Coursera", "rating": 4.6,
                 "url":"https://www.coursera.org/specializations/data-science-python",
                 "image_url":"https://d3njjcbhbojbot.cloudfront.net/api/utilities/v1/imageproxy/https://coursera-assets.s3.amazonaws.com/ads.jpg"},
            ]
        elif "software engineer" in role or "developer" in role:
            courses = [
                {"title": "Full Stack Web Development", "provider": "Coursera", "rating": 4.7,
                 "url":"https://www.coursera.org/specializations/full-stack",
                 "image_url":"https://d3njjcbhbojbot.cloudfront.net/api/utilities/v1/imageproxy/https://coursera-assets.s3.amazonaws.com/fswd.jpg"},
                {"title": "Data Structures & Algorithms", "provider": "Udemy", "rating": 4.6,
                 "url":"https://www.udemy.com/course/dsa",
                 "image_url":"https://www.udemy.com/staticx/udemy/images/course/dsa.jpg"},
                {"title": "Python for Everybody", "provider": "Coursera", "rating": 4.8,
                 "url":"https://www.coursera.org/specializations/python",
                 "image_url":"https://d3njjcbhbojbot.cloudfront.net/api/utilities/v1/imageproxy/https://coursera-assets.s3.amazonaws.com/python.jpg"},
            ]
        else:
            courses = [
                {"title": "Professional Development Course", "provider": "Coursera", "rating": 4.5,
                 "url":"https://www.coursera.org",
                 "image_url":"https://d3njjcbhbojbot.cloudfront.net/api/utilities/v1/imageproxy/https://coursera-assets.s3.amazonaws.com/prodev.jpg"},
            ]

    return {
        "ats_score": final_ats,
        "ats_breakdown": breakdown,
        "gemini_raw": gemini_result,
        "suggestions": gemini_result.get("suggestions", []),
        "strengths": gemini_result.get("strengths", []),
        "weaknesses": gemini_result.get("weaknesses", []),
        "course_recommendations": courses,
        "recommended_roles": gemini_result.get("recommended_roles", []),
        "role_courses": gemini_result.get("role_courses", [])
    }

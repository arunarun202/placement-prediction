# 🚀 Placement Predictor, Resume Evaluator & Career Assistant Web App

Welcome to the **Student Career Dashboard & Placement Predictor**! This is a feature-rich Django web application combined with a Bootstrap frontend, designed to help students evaluate their career readiness, predict placement outcomes, analyze resumes, and chat with an intelligent career assistant.

This project is ready to be cloned, set up, and run locally on any laptop.

---

## 🌟 Key Features

1. **User Authentication & Management**
   - Traditional register, login, and remember-me session controls.
   - Social OAuth login integration (Google and GitHub logins).
   - Custom user profiles with profile picture upload (Pillow resizing built-in) and bio management.
   - Safe password reset and change views via SMTP mail.

2. **Placement Predictor**
   - Takes input parameters: age, gender, qualification, cgpa, 10th & 12th percentages, internships, experience, target job roles, salary, soft skills, target company, etc.
   - Predicts placement success (`Yes`/`No`) and provides a percentage confidence score using a pre-trained machine learning model (`users/placement_new2.pkl`).
   - Integrates **Google Gemini 2.5 Flash API** to generate 5 personalized, actionable career recommendations based on the user's specific weak points and targets.

3. **ATS Resume Evaluator**
   - Accepts resume uploads in **PDF**, **DOCX (Word)**, and **TXT** formats.
   - Extracts text using custom backend engines (`pdfplumber` and `docx`).
   - Scores the resume via a composite pipeline:
     - *Heuristics*: Regex patterns check for contact info, formatting, skills, action verbs, education details, and metrics.
     - *AI Model*: Gemini 2.5 Flash parses the text to identify detailed strengths, weaknesses, and direct career suggestions.
   - Recommends customized online courses (from Coursera, Udemy, etc.) with clickable links and covers image fallbacks.
   - Displays a resume dashboard history.

4. **Intelligent Career Chatbot**
   - Powered by a Keras/TensorFlow model (`Chatbot/chatbot_modelJ.h5`) for quick question classification.
   - Uses `nltk` tokenization and lemmatization for query understanding.
   - Incorporates translation services (`googletrans`) supporting queries in multiple languages.
   - Provides text-to-speech output using `gTTS` and Pygame `mixer` to play the translated responses automatically.

---

## 📁 Project Structure

```text
Deploy/
├── Chatbot/                   # App handling the AI Chatbot
│   ├── processor.py           # Core chatbot logic (lemmatization, prediction, TTS)
│   ├── chatbot_modelJ.h5      # Keras deep learning model for chatbot classification
│   ├── wordsJ.pkl, classesJ.pkl # Pickled datasets for vocabulary mapping
│   ├── intents.json           # Defined chatbot intents & response configurations
│   └── views.py, urls.py, ... # Chatbot endpoints and views
├── user_management/           # Core Django settings folder
│   ├── settings.py            # Apps configurations, DB path, auth backends, mail setup
│   └── urls.py                # Main project routing
├── users/                     # App for authentication, placement model, and resume parsing
│   ├── resume_processor.py    # Resume text extraction (PDF/DOCX) & Gemini analysis
│   ├── placement_new2.pkl     # Pre-trained placement prediction ML model
│   ├── models.py              # Custom schemas for Profile, Predict history, Resume uploads
│   ├── forms.py               # Front-end forms (registration, login, profile, upload)
│   └── views.py, urls.py, ... # Views handling dashboard panels & ML inference
├── media/                     # Holds user uploads (profile images, uploaded resumes)
├── static/                    # Custom CSS, JS files, and assets
├── Responses/                 # Temp output folder for chatbot speech mp3s
├── db.sqlite3                 # Local SQLite database
├── manage.py                  # Django administrative script
├── a.py                       # Small utility script to download NLTK wordnet data
├── language keywords.txt      # Reference language codes for translator
├── .env.example               # Example env config template
├── .gitignore                 # Version control ignores
└── requirements.txt           # Main project Python dependencies
```

---

## 🛠️ Step-by-Step Installation Guide

Follow these steps to set up and run this project on a local machine/laptop:

### 1. Prerequisites
- Ensure **Python 3.9 to 3.11** is installed on your laptop. (Newer python versions might face compatibility issues with older TensorFlow/Keras libraries).
- Git installed (optional, to clone the project).

### 2. Set Up a Virtual Environment
Navigate to the project directory in your terminal/command prompt and run:
```bash
# Create a virtual environment named 'venv'
python -m venv venv

# Activate the virtual environment
# On Windows (Command Prompt):
venv\Scripts\activate

# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Required Dependencies
With the virtual environment activated, run:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
*(This will install Django, TensorFlow, Keras, Pillow, Google GenAI SDKs, NLTK, Pygame, pdfplumber, python-docx, and other necessary packages).*

### 4. Configure Environment Variables (`.env`)
The project utilizes several external integrations (Google Gemini API, Google/GitHub OAuth logins, SMTP Email).
1. Look at the `.env.example` file in the root directory.
2. Create a new file named `.env` in the root folder.
3. Add your values:
   ```env
   SECRET_KEY=your-django-secret-key
   
   # Gemini API Key (Required for resume scoring and placement suggestions)
   GEMINI_API_KEY=AIzaSy...your-actual-api-key

   # SMTP Email credentials (for password resets)
   EMAIL_USER=your-email@gmail.com
   EMAIL_PASSWORD=your-app-password
   
   # Social logins (optional, keep empty if not configured)
   GITHUB_KEY=your-github-id
   GITHUB_SECRET=your-github-secret
   GOOGLE_KEY=your-google-oauth-key
   GOOGLE_SECRET=your-google-oauth-secret
   ```

### 5. Download NLTK Datasets
The natural language chatbot requires specific NLTK tokenizer models. Run the provided helper script:
```bash
python a.py
```
If you encounter missing NLTK errors while running the chatbot, open a python shell and run:
```python
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
```

### 6. Set Up Database and Run Migrations
Generate and execute local database tables from Django's configuration:
```bash
# Apply migrations to your SQLite database
python manage.py migrate

# Create an admin account to access Django Admin Dashboard
python manage.py createsuperuser
```
Follow the prompts in the terminal to set up a username, email, and password for the admin panel.

### 7. Run the Server
Start the Django development server:
```bash
python manage.py runserver
```

Once running, open your web browser and navigate to:
👉 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

To access the backend administrator dashboard, go to:
👉 **[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)**

---

## ⚠️ Important Considerations & Troubleshooting

- **Gemini API Setup**: The application connects to `gemini-2.5-flash` for resume parser parsing and career recommendation. Ensure your `GEMINI_API_KEY` environment variable is valid and active.
- **Pygame Audio Driver**: To run headlessly on environments without speakers (like servers), the chatbot processor uses `os.environ["SDL_AUDIODRIVER"] = "dummy"` which prevents audio engine initialization failures.
- **Static & Media Files**: If profile pictures or resumes fail to upload/render, make sure the `media/` directory exists and has write permissions.

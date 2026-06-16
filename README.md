# 🚀 Placement Predictor & Career Assistant Web App (Phase 3)

Welcome to the **Student Career Dashboard & Placement Predictor**! This is a modern, decoupled web application featuring a FastAPI Python backend and a React (Vite) frontend. It is designed to help students evaluate their career readiness, predict placement outcomes, analyze resumes, and chat with an intelligent AI career assistant.

This project is fully dockerized and ready to be cloned, set up, and run locally on any machine.

---

## 🌟 Key Features

1. **User Authentication & Management**
   - JWT-based authentication (Register, Login, Session Management).
   - Custom user profiles and dashboard.

2. **Placement Predictor**
   - Takes input parameters: age, gender, qualification, cgpa, 10th & 12th percentages, internships, experience, target job roles, salary, soft skills, target company, etc.
   - Evaluates the statistics through an intelligent OpenRouter-powered prediction engine.
   - Provides a detailed **Predicted Score (0-100%)** and a personalized career explanation.

3. **ATS Resume Evaluator**
   - Accepts resume inputs and scores them against Applicant Tracking System (ATS) standards using advanced AI prompts.
   - Returns strict JSON evaluations detailing Match Score, Actionable Suggestions, and Recommended Courses.

4. **Intelligent Career Chatbot**
   - A fully contextual AI assistant designed to guide students with their career path, resume building, and interview preparation.
   - Maintains conversation history effortlessly for natural interactions.

---

## 📁 Project Structure

```text
Deploy/
├── backend/                   # FastAPI Backend Application
│   ├── app/                   # Core application logic (API routers, models, schemas, services)
│   ├── alembic/               # Database migration scripts
│   ├── requirements.txt       # Python dependencies
│   ├── Dockerfile             # Container configuration for the backend
│   └── .env.example           # Example environment variables
├── frontend/                  # React + Vite Frontend Application
│   ├── src/                   # React components, pages, and API hooks
│   ├── public/                # Static assets
│   ├── package.json           # Node dependencies
│   └── vercel.json            # Vercel deployment routing configuration
├── docker-compose.yml         # Orchestrates the backend and PostgreSQL containers
├── dbschema.sql               # Reference schema for the PostgreSQL database
└── README.md                  # Project documentation
```

---

## 🛠️ Step-by-Step Installation Guide

Follow these steps to set up and run this project on a local machine/laptop:

### 1. Prerequisites
- **Docker Desktop** installed and running on your machine.
- **Node.js** (v18+) and **npm** installed (for running the frontend).
- **Git** installed to clone the project.

### 2. Clone the Repository
```bash
git clone <your-repository-url>
cd Deploy
```

### 3. Backend Setup (Docker + FastAPI)
The backend and database run seamlessly using Docker Compose.

1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. Create your `.env` file by copying the template:
   ```bash
   cp .env.example .env
   ```
   *Make sure to add your OpenRouter API key (`OPENROUTER_API_KEY`) inside the `.env` file!*

3. Go back to the root directory and start the Docker containers:
   ```bash
   cd ..
   docker compose up --build -d
   ```
   *(This will download the PostgreSQL image, build the FastAPI backend, and start both services.)*

4. Run Database Migrations:
   Once the containers are up, initialize the database tables:
   ```bash
   docker exec local_fastapi_backend alembic upgrade head
   ```

Your backend API is now running at: **http://localhost:8000**
Interactive API Documentation (Swagger UI) is available at: **http://localhost:8000/docs**

### 4. Frontend Setup (React + Vite)
The frontend runs via Node.js and connects to your local FastAPI backend.

1. Open a new terminal and navigate to the `frontend` folder:
   ```bash
   cd frontend
   ```
2. Install the required Node dependencies:
   ```bash
   npm install
   ```
3. Start the Vite development server:
   ```bash
   npm run dev
   ```

Your frontend application is now running! Open your browser and navigate to the URL provided in the terminal (usually **http://localhost:5173**).

---

## ⚠️ Important Considerations & Troubleshooting

- **API Keys**: The application requires an `OPENROUTER_API_KEY` to function. If you get a "Failed to get response" error, double-check your `.env` file and ensure your OpenRouter account has access to the configured models.
- **Database Resets**: If you need to completely wipe your database and start over, you can delete the docker volume using `docker compose down -v` and run the build steps again.
- **Deployment**: For production deployment, the backend can be hosted on Render/Railway, and the frontend on Vercel (using the provided `vercel.json` for routing).

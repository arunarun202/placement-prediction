Here is the updated Product Requirements Document (PRD). It has been revised to remove the heavy local ML models, replace them with the OpenRouter API, and fully integrate the robust CI/CD and E2E testing pipeline architecture we mapped out.

You can hand this directly to your AI agent.

---

# Product Requirements Document (PRD)

## Project: Placement Predictor & Career Assistant - Stack Migration

### 1. Current Project Stage

The project is currently in the **Monolithic MVP (Minimum Viable Product)** stage.

* **Architecture**: Tightly coupled monolithic architecture built with Django.
* **Frontend**: Server-side rendered Django templates using Bootstrap.
* **Backend**: Django handling routing, authentication, file processing, and local ML model inference synchronously.
* **Database**: SQLite.
* **Functionality**: Core features are complete (User Management, Placement Prediction, ATS Resume Evaluation, and Chatbot).

### 2. Migration Goals

The goal is to modernize the tech stack to a **Decoupled Architecture** to ensure scalability, eliminate heavy local ML dependencies, and automate testing and deployment.

* **Frontend**: React + Vite (Fast builds, dynamic single-page application).
* **Backend**: FastAPI (High performance, async native, perfect for handling external AI API calls).
* **Database**: PostgreSQL using a local Docker container for development/testing, and Supabase (as a managed Postgres DB like AWS RDS) for production.
* **AI Engine**: OpenRouter API (Replacing heavy local `.pkl` and `.h5` models with cloud-based LLMs).
* **CI/CD & Quality Assurance**: GitHub Actions acting as the central pipeline to generate automated End-to-End (E2E) testing reports before deployment.

---

## 3. Step-by-Step Migration Plan

### Phase 1: Database Setup (PostgreSQL)

**Objective**: Set up the relational database foundation without relying on Backend-as-a-Service features.

* **Local Dev**: Create a `docker-compose.yml` to spin up a local PostgreSQL (`postgres:15-alpine`) database container for offline development.
* **Production/Cloud**: Set up a Supabase project. Extract the direct Postgres connection string. **Crucial:** Do not utilize Supabase's Data APIs or auto-generated Row Level Security (RLS). All database access will be securely managed by FastAPI.
* **Schema Design**: Map existing Django models (Users, Profiles, Predictions, Resume Uploads) to SQLAlchemy ORM models.
* **Migrations**: Set up `Alembic` for handling database schema migrations.

### Phase 2: Backend Development (FastAPI)

**Objective**: Rebuild the backend as a pure REST API and swap local ML models for external APIs.

* **Project Structure**: Set up FastAPI in a `/backend` directory with a modular router structure (e.g., `/auth`, `/predict`, `/resume`, `/chat`).
* **Authentication**: Implement JWT-based authentication managed natively by FastAPI.
* **Database ORM**: Integrate SQLAlchemy and connect it to the PostgreSQL database using standard connection URIs.
* **AI & Inference Migration (OpenRouter)**:
* **Placement Prediction**: Deprecate `placement_new2.pkl`. Create an async endpoint that formats user statistics into a prompt and sends it to the OpenRouter API for evaluation and recommendations.
* **Resume Parsing**: Keep `pdfplumber`/`python-docx` for text extraction, but send the extracted text to OpenRouter/Gemini for ATS evaluation via async FastAPI routes.
* **Chatbot**: Deprecate the Keras model (`chatbot_modelJ.h5`) and NLTK logic. Create an async chat endpoint that streams responses directly from OpenRouter.


* **Media & File Handling**: Implement robust file upload endpoints for resumes using `UploadFile` in FastAPI.

### Phase 3: Frontend Development (React + Vite)

**Objective**: Build a dynamic, responsive Single Page Application (SPA).

* **Initialization**: Create a project in the `/frontend` directory using Vite.
* **State Management & Routing**: Set up `react-router-dom` for navigation and Zustand or React Context for user sessions.
* **API Client**: Create a centralized Axios instance to handle base URLs, JWT token injection, and async states.
* **Component Breakdown**:
* `Auth`: Login, Register, Profile.
* `Dashboard`: User history, recent predictions, and resume scores.
* `PlacementPredictor`: Form for inputting stats and displaying the OpenRouter prediction result.
* `ResumeEvaluator`: Drag-and-drop file upload, loading states, and detailed score breakdown view.
* `Chatbot`: Floating action button opening a chat window with a modern messaging UI.



### Phase 4: E2E Testing & CI Pipeline (GitHub Actions)

**Objective**: Automate quality assurance and fulfill academic reporting requirements without polluting the production database.

* **Testing Framework**: Install and configure **Playwright** in a `/tests` directory.
* **The Sandbox CI Environment**: Create a GitHub Actions workflow (`.github/workflows/e2e.yml`) that triggers on push.
1. Spins up a temporary PostgreSQL service container directly inside the GitHub Runner.
2. Installs and starts the FastAPI backend, pointing its `DATABASE_URL` to the temporary runner database.
3. Installs and starts the React frontend in the background.
4. Executes the Playwright E2E test suite against these local servers.


* **Reporting**: The GitHub Action must format the test results and use `actions/upload-artifact` to attach a `.csv` or `.xlsx` execution log to every commit.

### Phase 5: Deployment Strategy

**Objective**: Take the application to production using parallel deployment pipelines.

* **Database**: Apply Alembic migrations to the production Supabase Postgres instance.
* **Backend (Render)**:
* Write a `Dockerfile` in the `/backend` directory.
* Deploy to Render as a Web Service utilizing the Docker environment. Configure environment variables for Supabase DB, OpenRouter API keys, and CORS origins.


* **Frontend (Vercel / GitHub Pages)**:
* Deploy the `/frontend` directory to Vercel (or use GitHub Actions to deploy to GitHub Pages, depending on course requirements).
* Update the frontend `.env` to point to the live Render backend URL.
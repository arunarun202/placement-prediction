-- PostgreSQL Database Schema for Placement Predictor

-- 1. Users Table (Mirroring Django's auth_user to our new FastAPI structure)
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(150) UNIQUE NOT NULL,
    password VARCHAR(128) NOT NULL,
    email VARCHAR(254) UNIQUE,
    first_name VARCHAR(150) DEFAULT '',
    last_name VARCHAR(150) DEFAULT '',
    is_active BOOLEAN DEFAULT TRUE,
    is_superuser BOOLEAN DEFAULT FALSE,
    date_joined TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2. Profiles Table
CREATE TABLE IF NOT EXISTS profiles (
    id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    avatar VARCHAR(255) DEFAULT 'default.jpg',
    bio TEXT DEFAULT ''
);

-- 3. Chatbot History Table
CREATE TABLE IF NOT EXISTS chatbots (
    id SERIAL PRIMARY KEY,
    message TEXT NOT NULL
);

-- 4. User Predict Model (Predictions History)
CREATE TABLE IF NOT EXISTS user_predict_models (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    age DOUBLE PRECISION NOT NULL,
    gender VARCHAR(20) NOT NULL,
    qualification VARCHAR(50) NOT NULL,
    year DOUBLE PRECISION NOT NULL,
    cgpa DOUBLE PRECISION NOT NULL,
    job_role VARCHAR(50) NOT NULL,
    post_graduation VARCHAR(20) NOT NULL,
    ten_percentage DOUBLE PRECISION NOT NULL,
    twelth_percentage DOUBLE PRECISION NOT NULL,
    salary DOUBLE PRECISION NOT NULL,
    soft_skills VARCHAR(50) NOT NULL,
    internship VARCHAR(50) NOT NULL,
    experience DOUBLE PRECISION NOT NULL,
    round INTEGER NOT NULL,
    company_name VARCHAR(100) NOT NULL,
    label VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 5. Resume Uploads Table
CREATE TABLE IF NOT EXISTS resume_uploads (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(254),
    job_role VARCHAR(255),
    uploaded_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    file VARCHAR(255) NOT NULL,
    processed BOOLEAN DEFAULT FALSE,
    ats_score DOUBLE PRECISION,
    gemini_response JSONB,
    suggestions TEXT,
    course_products JSONB,
    alternative_roles JSONB,
    role_courses JSONB
);

-- Indexes for performance
CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);
CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
CREATE INDEX IF NOT EXISTS idx_user_predict_models_user_id ON user_predict_models(user_id);
CREATE INDEX IF NOT EXISTS idx_resume_uploads_user_id ON resume_uploads(user_id);

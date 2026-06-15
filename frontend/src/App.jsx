import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Toaster } from 'react-hot-toast';
import { AuthProvider } from './context/AuthContext';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import ProtectedRoute from './components/ProtectedRoute';

// Pages
import HomePage from './pages/HomePage';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import ProfilePage from './pages/ProfilePage';
import PredictionPage from './pages/PredictionPage';
import PredictionResult from './pages/PredictionResult';
import PredictionHistory from './pages/PredictionHistory';
import ResumeUploadPage from './pages/ResumeUploadPage';
import ResumeResultPage from './pages/ResumeResultPage';
import ResumeListPage from './pages/ResumeListPage';
import ChatbotPage from './pages/ChatbotPage';
import NotFoundPage from './pages/NotFoundPage';

function App() {
  return (
    <AuthProvider>
      <Router>
        <div className="flex flex-col min-h-screen">
          <Navbar />
          <main className="flex-grow">
            <Routes>
              {/* Public Routes */}
              <Route path="/" element={<HomePage />} />
              <Route path="/login" element={<LoginPage />} />
              <Route path="/register" element={<RegisterPage />} />
              
              {/* Protected Routes */}
              <Route element={<ProtectedRoute />}>
                <Route path="/profile" element={<ProfilePage />} />
                
                <Route path="/predict" element={<PredictionPage />} />
                <Route path="/prediction/result" element={<PredictionResult />} />
                <Route path="/predictions" element={<PredictionHistory />} />
                
                <Route path="/resume" element={<ResumeUploadPage />} />
                <Route path="/resume/result/:id" element={<ResumeResultPage />} />
                <Route path="/resumes" element={<ResumeListPage />} />
                
                <Route path="/chatbot" element={<ChatbotPage />} />
              </Route>

              {/* 404 Route */}
              <Route path="*" element={<NotFoundPage />} />
            </Routes>
          </main>
          <Footer />
        </div>
        <Toaster position="top-right" />
      </Router>
    </AuthProvider>
  );
}

export default App;

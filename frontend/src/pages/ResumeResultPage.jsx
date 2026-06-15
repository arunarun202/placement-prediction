import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { motion } from 'framer-motion';
import { FaTrophy, FaLightbulb, FaBriefcase, FaGraduationCap, FaArrowLeft, FaFilePdf, FaRobot } from 'react-icons/fa';
import api from '../api/axios';
import LoadingSpinner from '../components/LoadingSpinner';
import { toast } from 'react-hot-toast';

const ResumeResultPage = () => {
  const { id } = useParams();
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchResult = async () => {
      try {
        const response = await api.get(`/resume/${id}/`);
        setResult(response.data);
      } catch (error) {
        toast.error('Failed to load resume analysis');
        console.error(error);
      } finally {
        setLoading(false);
      }
    };
    fetchResult();
  }, [id]);

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-slate-50">
        <LoadingSpinner text="Loading Analysis..." />
      </div>
    );
  }

  if (!result) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-slate-50">
        <div className="text-center">
          <h2 className="text-2xl font-bold text-slate-800">Result not found</h2>
          <Link to="/resume" className="text-[var(--color-brand-primary)] hover:underline mt-4 inline-block">Go back to upload</Link>
        </div>
      </div>
    );
  }

  const { resume, ats_score, suggestions, course_recommendations, roles } = result;
  
  // Determine score color
  const getScoreColor = (score) => {
    if (score >= 80) return 'text-green-500 stroke-green-500';
    if (score >= 60) return 'text-yellow-500 stroke-yellow-500';
    return 'text-red-500 stroke-red-500';
  };

  const getScoreBg = (score) => {
    if (score >= 80) return 'bg-green-50 border-green-500';
    if (score >= 60) return 'bg-yellow-50 border-yellow-500';
    return 'bg-red-50 border-red-500';
  };

  return (
    <div className="min-h-screen bg-slate-50 pt-10 pb-20">
      <div className="max-w-6xl mx-auto px-4">
        <div className="mb-8">
          <Link to="/resumes" className="text-slate-500 hover:text-[var(--color-brand-primary)] flex items-center gap-2 transition-colors w-max">
            <FaArrowLeft /> Back to Resumes
          </Link>
        </div>

        {/* Header & Score Section */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-8">
          <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className={`col-span-1 lg:col-span-1 rounded-3xl p-8 border-t-8 shadow-xl flex flex-col items-center justify-center text-center ${getScoreBg(ats_score)}`}
          >
            <h2 className="text-2xl font-bold text-slate-800 mb-6">ATS Compatibility</h2>
            
            <div className="relative w-48 h-48 mb-4">
              <svg viewBox="0 0 100 100" className="w-full h-full transform -rotate-90">
                <circle cx="50" cy="50" r="45" fill="none" stroke="#e2e8f0" strokeWidth="8" />
                <circle 
                  cx="50" cy="50" r="45" fill="none" 
                  strokeWidth="8" 
                  strokeDasharray={`${ats_score * 2.827} 282.7`} 
                  strokeLinecap="round" 
                  className={`transition-all duration-1000 ease-out ${getScoreColor(ats_score).split(' ')[1]}`}
                />
              </svg>
              <div className="absolute inset-0 flex flex-col items-center justify-center">
                <span className={`text-5xl font-black ${getScoreColor(ats_score).split(' ')[0]}`}>
                  {ats_score}%
                </span>
              </div>
            </div>
            
            <p className="text-slate-700 font-medium mt-4">
              {ats_score >= 80 ? "Excellent! Your resume is highly ATS-friendly." : 
               ats_score >= 60 ? "Good, but needs some optimization." : 
               "Needs significant improvement to pass ATS filters."}
            </p>
          </motion.div>

          <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.1 }}
            className="col-span-1 lg:col-span-2 bg-white rounded-3xl p-8 shadow-xl border border-slate-100"
          >
            <div className="flex justify-between items-start mb-6">
              <div>
                <h2 className="text-2xl font-bold text-slate-800 mb-1">Resume Details</h2>
                <p className="text-slate-500">Target Role: <span className="font-semibold text-slate-700">{resume.job_role}</span></p>
              </div>
              <div className="w-12 h-12 bg-orange-100 rounded-xl flex items-center justify-center text-[var(--color-brand-primary)]">
                <FaFilePdf className="text-2xl" />
              </div>
            </div>

            <div className="space-y-6">
              <div>
                <h3 className="text-lg font-bold text-slate-800 mb-3 flex items-center gap-2">
                  <FaLightbulb className="text-yellow-500" /> Key Suggestions
                </h3>
                <ul className="space-y-3">
                  {suggestions.slice(0, 5).map((suggestion, index) => (
                    <li key={index} className="flex items-start gap-3 text-slate-700 bg-slate-50 p-3 rounded-xl border border-slate-100">
                      <span className="text-[var(--color-brand-primary)] mt-1">•</span>
                      <span>{suggestion}</span>
                    </li>
                  ))}
                  {suggestions.length === 0 && (
                    <p className="text-slate-500 italic">No specific suggestions available.</p>
                  )}
                </ul>
              </div>
            </div>
          </motion.div>
        </div>

        {/* Recommendations Section */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {/* Roles */}
          <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.2 }}
            className="bg-white rounded-3xl p-8 shadow-xl border border-slate-100"
          >
            <h3 className="text-xl font-bold text-slate-800 mb-6 flex items-center gap-3 pb-4 border-b border-slate-100">
              <FaBriefcase className="text-[var(--color-brand-primary)]" /> 
              Alternative Roles to Consider
            </h3>
            
            <div className="flex flex-wrap gap-3">
              {roles.map((role, index) => (
                <div key={index} className="bg-slate-50 border border-slate-200 text-slate-700 px-4 py-2 rounded-full font-medium hover:bg-orange-50 hover:text-[var(--color-brand-primary)] hover:border-orange-200 transition-colors cursor-pointer">
                  {role}
                </div>
              ))}
              {roles.length === 0 && (
                <p className="text-slate-500">No alternative roles generated.</p>
              )}
            </div>
          </motion.div>

          {/* Courses */}
          <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.3 }}
            className="bg-white rounded-3xl p-8 shadow-xl border border-slate-100"
          >
            <h3 className="text-xl font-bold text-slate-800 mb-6 flex items-center gap-3 pb-4 border-b border-slate-100">
              <FaGraduationCap className="text-[var(--color-brand-primary)]" /> 
              Recommended Courses
            </h3>
            
            <div className="space-y-4">
              {course_recommendations.map((course, index) => (
                <div key={index} className="flex items-center justify-between bg-slate-50 p-4 rounded-xl border border-slate-100 hover:shadow-md transition-shadow">
                  <div className="flex items-center gap-3">
                    <div className="w-10 h-10 bg-orange-100 rounded-lg flex items-center justify-center shrink-0">
                      <FaTrophy className="text-[var(--color-brand-primary)]" />
                    </div>
                    <span className="font-semibold text-slate-700">{course}</span>
                  </div>
                  <button className="text-[var(--color-brand-primary)] font-medium text-sm hover:underline whitespace-nowrap ml-4">
                    View Course
                  </button>
                </div>
              ))}
              {course_recommendations.length === 0 && (
                <p className="text-slate-500">No courses recommended.</p>
              )}
            </div>
          </motion.div>
        </div>
      </div>
    </div>
  );
};

export default ResumeResultPage;

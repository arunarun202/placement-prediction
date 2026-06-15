import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { motion } from 'framer-motion';
import { FaFileAlt, FaTrash, FaEye, FaArrowRight, FaFilePdf } from 'react-icons/fa';
import api from '../api/axios';
import LoadingSpinner from '../components/LoadingSpinner';
import { toast } from 'react-hot-toast';

const ResumeListPage = () => {
  const [resumes, setResumes] = useState([]);
  const [loading, setLoading] = useState(true);

  const fetchResumes = async () => {
    try {
      const response = await api.get('/resumes/');
      setResumes(response.data);
    } catch (error) {
      toast.error('Failed to load saved resumes');
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchResumes();
  }, []);

  const handleDelete = async (id) => {
    if (window.confirm("Are you sure you want to delete this resume analysis?")) {
      try {
        await api.delete(`/resume/${id}/delete/`);
        toast.success('Resume deleted successfully');
        fetchResumes();
      } catch (error) {
        toast.error('Failed to delete resume');
      }
    }
  };

  const formatDate = (dateString) => {
    const options = { year: 'numeric', month: 'short', day: 'numeric' };
    return new Date(dateString).toLocaleDateString(undefined, options);
  };

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-slate-50">
        <LoadingSpinner text="Loading Resumes..." />
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-50 pt-10 pb-20">
      <div className="max-w-6xl mx-auto px-4">
        <div className="flex justify-between items-center mb-8">
          <div>
            <h1 className="text-3xl font-extrabold text-slate-800 tracking-tight flex items-center gap-3">
              <FaFileAlt className="text-[var(--color-brand-primary)]" /> Saved Resumes
            </h1>
            <p className="mt-2 text-slate-600">Access your past resume analyses and ATS scores.</p>
          </div>
          <Link to="/resume" className="hidden md:flex bg-[var(--color-brand-primary)] hover:bg-[var(--color-brand-secondary)] text-white px-6 py-2.5 rounded-full font-medium transition-colors items-center gap-2">
            Upload New <FaArrowRight />
          </Link>
        </div>

        {resumes.length === 0 ? (
          <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="bg-white rounded-3xl shadow-xl p-12 text-center border border-slate-100"
          >
            <div className="w-20 h-20 bg-orange-50 rounded-full flex items-center justify-center mx-auto mb-4">
              <FaFileAlt className="text-3xl text-slate-400" />
            </div>
            <h3 className="text-xl font-bold text-slate-800 mb-2">No Resumes Found</h3>
            <p className="text-slate-500 mb-6 max-w-md mx-auto">
              You haven't analyzed any resumes yet. Upload your resume to get an ATS score and AI feedback.
            </p>
            <Link to="/resume" className="inline-block bg-[var(--color-brand-primary)] text-white px-8 py-3 rounded-full font-bold shadow-md hover:shadow-lg transition-all">
              Analyze Resume
            </Link>
          </motion.div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {resumes.map((resume, index) => (
              <motion.div 
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: index * 0.1 }}
                key={resume.id}
                className="bg-white rounded-3xl shadow-lg border border-slate-100 overflow-hidden hover:shadow-xl transition-shadow"
              >
                <div className="p-6">
                  <div className="flex justify-between items-start mb-4">
                    <div className="w-12 h-12 bg-orange-50 rounded-xl flex items-center justify-center text-[var(--color-brand-primary)]">
                      <FaFilePdf className="text-2xl" />
                    </div>
                    <div className={`px-3 py-1 rounded-full text-xs font-bold ${
                      resume.ats_score >= 80 ? 'bg-green-100 text-green-700' :
                      resume.ats_score >= 60 ? 'bg-yellow-100 text-yellow-700' :
                      'bg-red-100 text-red-700'
                    }`}>
                      ATS: {resume.ats_score}%
                    </div>
                  </div>
                  
                  <h3 className="text-lg font-bold text-slate-800 truncate mb-1" title={resume.name || "Unnamed Resume"}>
                    {resume.name || "Unnamed Resume"}
                  </h3>
                  <p className="text-sm text-[var(--color-brand-primary)] font-medium mb-4 truncate">
                    {resume.job_role || "No target role specified"}
                  </p>
                  
                  <p className="text-xs text-slate-500 mb-6 flex items-center gap-1">
                    Uploaded: {formatDate(resume.uploaded_at)}
                  </p>
                </div>
                
                <div className="flex border-t border-slate-100 bg-slate-50">
                  <Link to={`/resume/result/${resume.id}`} className="flex-1 py-3 text-center text-slate-700 font-medium hover:bg-white hover:text-[var(--color-brand-primary)] transition-colors border-r border-slate-100 flex justify-center items-center gap-2">
                    <FaEye /> View
                  </Link>
                  <button 
                    onClick={() => handleDelete(resume.id)}
                    className="flex-1 py-3 text-center text-red-500 font-medium hover:bg-red-50 transition-colors flex justify-center items-center gap-2"
                  >
                    <FaTrash /> Delete
                  </button>
                </div>
              </motion.div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default ResumeListPage;

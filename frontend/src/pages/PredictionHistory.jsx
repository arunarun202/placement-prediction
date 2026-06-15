import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { motion } from 'framer-motion';
import { FaHistory, FaCheckCircle, FaExclamationTriangle, FaEye, FaArrowRight } from 'react-icons/fa';
import api from '../api/axios';
import LoadingSpinner from '../components/LoadingSpinner';
import { toast } from 'react-hot-toast';

const PredictionHistory = () => {
  const [predictions, setPredictions] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchPredictions = async () => {
      try {
        const response = await api.get('/predictions/');
        setPredictions(response.data);
      } catch (error) {
        toast.error('Failed to load prediction history');
        console.error(error);
      } finally {
        setLoading(false);
      }
    };
    fetchPredictions();
  }, []);

  const formatDate = (dateString) => {
    const options = { year: 'numeric', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' };
    return new Date(dateString).toLocaleDateString(undefined, options);
  };

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-slate-50">
        <LoadingSpinner text="Loading History..." />
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-50 pt-10 pb-20">
      <div className="max-w-6xl mx-auto px-4">
        <div className="flex justify-between items-center mb-8">
          <div>
            <h1 className="text-3xl font-extrabold text-slate-800 tracking-tight flex items-center gap-3">
              <FaHistory className="text-[var(--color-brand-primary)]" /> Prediction History
            </h1>
            <p className="mt-2 text-slate-600">Track your progress and past placement predictions.</p>
          </div>
          <Link to="/predict" className="hidden md:flex bg-[var(--color-brand-primary)] hover:bg-[var(--color-brand-secondary)] text-white px-6 py-2.5 rounded-full font-medium transition-colors items-center gap-2">
            New Prediction <FaArrowRight />
          </Link>
        </div>

        {predictions.length === 0 ? (
          <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="bg-white rounded-3xl shadow-xl p-12 text-center border border-slate-100"
          >
            <div className="w-20 h-20 bg-orange-50 rounded-full flex items-center justify-center mx-auto mb-4">
              <FaHistory className="text-3xl text-slate-400" />
            </div>
            <h3 className="text-xl font-bold text-slate-800 mb-2">No Predictions Yet</h3>
            <p className="text-slate-500 mb-6 max-w-md mx-auto">
              You haven't run any placement predictions. Try predicting your chances to see your history here.
            </p>
            <Link to="/predict" className="inline-block bg-[var(--color-brand-primary)] text-white px-8 py-3 rounded-full font-bold shadow-md hover:shadow-lg transition-all">
              Start Prediction
            </Link>
          </motion.div>
        ) : (
          <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="bg-white rounded-3xl shadow-xl overflow-hidden border border-slate-100"
          >
            <div className="overflow-x-auto">
              <table className="w-full text-left border-collapse">
                <thead>
                  <tr className="bg-slate-50 border-b border-slate-200 text-slate-600 uppercase tracking-wider text-xs font-semibold">
                    <th className="px-6 py-4">Date & Time</th>
                    <th className="px-6 py-4">Target Role</th>
                    <th className="px-6 py-4">Company</th>
                    <th className="px-6 py-4">Status</th>
                    <th className="px-6 py-4 text-center">Actions</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-100">
                  {predictions.map((pred) => (
                    <tr key={pred.id} className="hover:bg-slate-50 transition-colors">
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-slate-700 font-medium">
                        {formatDate(pred.created_at)}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-slate-700">
                        {['Android Studio', 'C', 'C++', 'Data Analytics', 'Data Science', 'Frontend', 'Full Stack', 'Java', 'Node JS', 'Python', 'React'][pred.Job_Role]}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-slate-700">
                        {['Accenture', 'Amazon', 'Amul', 'Asian Paints', 'Axis Bank', 'Bajaj', 'BigBasket', 'Bosch', 'Byjus', 'Capgemini', 'Cognizant'][Math.min(pred.Company_Name, 10)]}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap">
                        <span className={`inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold ${
                          pred.label.toLowerCase() === 'yes' 
                            ? 'bg-green-100 text-green-700' 
                            : 'bg-red-100 text-red-700'
                        }`}>
                          {pred.label.toLowerCase() === 'yes' ? <FaCheckCircle /> : <FaExclamationTriangle />}
                          {pred.label.toUpperCase()}
                        </span>
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-center">
                        <button className="text-[var(--color-brand-primary)] hover:text-[var(--color-brand-secondary)] font-medium text-sm flex items-center justify-center gap-2 mx-auto transition-colors"
                          onClick={() => toast('Detailed view not implemented yet. Try running a new prediction!', { icon: 'ℹ️' })}
                        >
                          <FaEye /> View
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </motion.div>
        )}
      </div>
    </div>
  );
};

export default PredictionHistory;

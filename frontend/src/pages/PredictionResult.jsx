import React, { useEffect } from 'react';
import { useLocation, useNavigate, Link } from 'react-router-dom';
import { motion } from 'framer-motion';
import { FaChartLine, FaCheckCircle, FaExclamationTriangle, FaRedo, FaBullseye } from 'react-icons/fa';
import { Doughnut, Radar, Bar, Line } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  RadialLinearScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip,
  Legend,
  ArcElement,
  CategoryScale,
  LinearScale,
  BarElement
} from 'chart.js';

ChartJS.register(
  RadialLinearScale, PointElement, LineElement, Filler, Tooltip, Legend, 
  ArcElement, CategoryScale, LinearScale, BarElement
);

const PredictionResult = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const result = location.state?.result;

  useEffect(() => {
    if (!result) {
      navigate('/predict');
    }
  }, [result, navigate]);

  if (!result) return null;

  const { prediction, probability, prediction_breakdown, recommendations } = result;
  const isSuccess = prediction.toLowerCase() === 'yes';

  // Chart Data Configurations
  const radarData = {
    labels: ['Technical', 'Academics', 'Experience', 'Company Fit'],
    datasets: [{
      label: 'Your Score',
      data: [
        prediction_breakdown.skill_score,
        prediction_breakdown.academic_score,
        prediction_breakdown.experience_score,
        prediction_breakdown.company_fit
      ],
      backgroundColor: 'rgba(255, 107, 53, 0.2)',
      borderColor: 'rgba(255, 107, 53, 1)',
      borderWidth: 2,
    }]
  };

  const doughnutData = {
    labels: ['Academics', 'Technical', 'Experience', 'Fit'],
    datasets: [{
      data: [35, 25, 20, 20],
      backgroundColor: ['#FF6B35', '#FF8C00', '#FFA500', '#FFB74D'],
      borderWidth: 0
    }]
  };

  const lineData = {
    labels: ['Now', '1 Mo', '2 Mo', '3 Mo', '4 Mo', '5 Mo'],
    datasets: [{
      label: 'Growth Trajectory',
      data: [
        probability, 
        Math.min(probability + 10, 95),
        Math.min(probability + 20, 98),
        Math.min(probability + 30, 99),
        Math.min(probability + 40, 99.5),
        99.9
      ],
      borderColor: '#FF6B35',
      backgroundColor: 'rgba(255, 107, 53, 0.1)',
      fill: true,
      tension: 0.4
    }]
  };

  return (
    <div className="min-h-screen bg-slate-50 pt-10 pb-20">
      <div className="max-w-6xl mx-auto px-4">
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="bg-white rounded-3xl shadow-xl p-8 mb-8"
        >
          {/* Header */}
          <div className="text-center mb-10">
            <h2 className="text-3xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-[var(--color-brand-primary)] to-[var(--color-brand-secondary)] mb-2">
              <FaChartLine className="inline mr-2 text-slate-800" /> Analysis Complete
            </h2>
          </div>

          {/* Result Card */}
          <div className={`rounded-2xl p-8 mb-10 border-l-8 ${isSuccess ? 'bg-green-50 border-green-500' : 'bg-red-50 border-red-500'}`}>
            <div className="flex flex-col md:flex-row items-center gap-8">
              <div className="w-48 h-48 relative shrink-0">
                <svg viewBox="0 0 100 100" className="w-full h-full transform -rotate-90">
                  <circle cx="50" cy="50" r="45" fill="none" stroke="#e2e8f0" strokeWidth="8" />
                  <circle cx="50" cy="50" r="45" fill="none" 
                    stroke={isSuccess ? "#22c55e" : "#ef4444"} 
                    strokeWidth="8" 
                    strokeDasharray={`${probability * 2.827} 282.7`} 
                    strokeLinecap="round" 
                    className="transition-all duration-1000 ease-out"
                  />
                </svg>
                <div className="absolute inset-0 flex flex-col items-center justify-center">
                  <span className={`text-4xl font-black ${isSuccess ? 'text-green-500' : 'text-red-500'}`}>
                    {Math.round(probability)}%
                  </span>
                  <span className="text-xs text-slate-500 font-medium">Probability</span>
                </div>
              </div>
              
              <div>
                <h3 className={`text-2xl font-bold mb-3 flex items-center gap-2 ${isSuccess ? 'text-green-700' : 'text-red-700'}`}>
                  {isSuccess ? <><FaCheckCircle /> Excellent Profile!</> : <><FaExclamationTriangle /> Needs Improvement</>}
                </h3>
                <p className="text-lg text-slate-700">
                  {isSuccess 
                    ? "Based on our model, your qualifications align strongly with industry requirements. You have a very high chance of getting placed!" 
                    : "Your profile currently shows areas for enhancement. With focused improvement on the factors below, you can significantly increase your chances."}
                </p>
              </div>
            </div>
          </div>

          {/* Stats Grid */}
          <div className="grid grid-cols-2 md:grid-cols-4 gap-6 mb-10">
            <div className="bg-slate-50 rounded-2xl p-6 text-center border-t-4 border-[var(--color-brand-primary)] shadow-sm">
              <div className="text-3xl font-black text-[var(--color-brand-primary)] mb-1">{prediction_breakdown.academic_score}%</div>
              <div className="text-sm font-semibold text-slate-600">Academic Score</div>
            </div>
            <div className="bg-slate-50 rounded-2xl p-6 text-center border-t-4 border-[var(--color-brand-primary)] shadow-sm">
              <div className="text-3xl font-black text-[var(--color-brand-primary)] mb-1">{prediction_breakdown.skill_score}%</div>
              <div className="text-sm font-semibold text-slate-600">Skill Match</div>
            </div>
            <div className="bg-slate-50 rounded-2xl p-6 text-center border-t-4 border-[var(--color-brand-primary)] shadow-sm">
              <div className="text-3xl font-black text-[var(--color-brand-primary)] mb-1">{prediction_breakdown.experience_score}%</div>
              <div className="text-sm font-semibold text-slate-600">Experience</div>
            </div>
            <div className="bg-slate-50 rounded-2xl p-6 text-center border-t-4 border-[var(--color-brand-primary)] shadow-sm">
              <div className="text-3xl font-black text-[var(--color-brand-primary)] mb-1">{prediction_breakdown.company_fit}%</div>
              <div className="text-sm font-semibold text-slate-600">Company Fit</div>
            </div>
          </div>

          {/* Charts Row */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-10">
            <div className="bg-white p-6 rounded-2xl shadow-[0_4px_20px_rgba(0,0,0,0.05)] border border-slate-100">
              <h4 className="font-bold text-center mb-4 text-slate-800">Skill Competency</h4>
              <div className="h-64"><Radar data={radarData} options={{ maintainAspectRatio: false }} /></div>
            </div>
            <div className="bg-white p-6 rounded-2xl shadow-[0_4px_20px_rgba(0,0,0,0.05)] border border-slate-100">
              <h4 className="font-bold text-center mb-4 text-slate-800">Factor Contribution</h4>
              <div className="h-64"><Doughnut data={doughnutData} options={{ maintainAspectRatio: false }} /></div>
            </div>
            <div className="bg-white p-6 rounded-2xl shadow-[0_4px_20px_rgba(0,0,0,0.05)] border border-slate-100 lg:col-span-1 md:col-span-2">
              <h4 className="font-bold text-center mb-4 text-slate-800">Projected Trajectory</h4>
              <div className="h-64"><Line data={lineData} options={{ maintainAspectRatio: false, scales: { y: { max: 100 } } }} /></div>
            </div>
          </div>

          {/* AI Recommendations */}
          <div className="bg-gradient-to-br from-slate-900 to-slate-800 rounded-2xl p-8 text-white">
            <h4 className="text-2xl font-bold mb-6 flex items-center gap-3">
              <FaBullseye className="text-[var(--color-brand-secondary)]" /> AI Recommendations
            </h4>
            <ul className="space-y-4">
              {recommendations.map((rec, index) => (
                <motion.li 
                  initial={{ opacity: 0, x: -20 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: 0.5 + (index * 0.1) }}
                  key={index} 
                  className="flex items-start gap-3 bg-white/10 p-4 rounded-xl border border-white/5"
                >
                  <FaCheckCircle className="text-[var(--color-brand-secondary)] mt-1 shrink-0" />
                  <span className="text-slate-200">{rec}</span>
                </motion.li>
              ))}
            </ul>
          </div>

          <div className="mt-10 flex justify-center">
            <Link to="/predict" className="btn bg-gradient-to-r from-[var(--color-brand-primary)] to-[var(--color-brand-secondary)] text-white px-8 py-3 rounded-full font-bold shadow-lg hover:shadow-orange-500/40 hover:-translate-y-1 transition-all flex items-center gap-2">
              <FaRedo /> Run New Prediction
            </Link>
          </div>
        </motion.div>
      </div>
    </div>
  );
};

export default PredictionResult;

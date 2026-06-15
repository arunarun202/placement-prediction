import React, { useState, useEffect, useRef } from 'react';
import { motion } from 'framer-motion';
import { FaPaperPlane, FaRobot, FaUserCircle } from 'react-icons/fa';
import api from '../api/axios';
import { toast } from 'react-hot-toast';

const ChatbotPage = () => {
  const [messages, setMessages] = useState([
    { id: 1, text: "Hi there 🖐. I'm PredictAI's Career Assistant. How can I help you today?", sender: 'bot' }
  ]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage = { id: Date.now(), text: input, sender: 'user' };
    setMessages(prev => [...prev, userMessage]);
    setInput('');
    setLoading(true);

    try {
      const response = await api.post('/chatbot/', { question: userMessage.text });
      const botMessage = { id: Date.now() + 1, text: response.data.response, sender: 'bot' };
      setMessages(prev => [...prev, botMessage]);
    } catch (error) {
      console.error(error);
      const errorMessage = { id: Date.now() + 1, text: "Sorry, I'm having trouble connecting to the server. Please try again later.", sender: 'bot' };
      setMessages(prev => [...prev, errorMessage]);
      toast.error('Failed to get response');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-50 flex flex-col py-8">
      <div className="max-w-4xl mx-auto w-full px-4 flex-grow flex flex-col">
        <div className="text-center mb-6">
          <h1 className="text-3xl font-extrabold text-slate-800">
            Career <span className="text-[var(--color-brand-primary)]">Assistant</span>
          </h1>
          <p className="text-slate-600 mt-2">Ask questions about interviews, resumes, or career paths.</p>
        </div>

        <div className="flex-grow bg-white rounded-3xl shadow-xl border border-slate-200 overflow-hidden flex flex-col h-[600px]">
          {/* Header */}
          <div className="bg-slate-900 px-6 py-4 flex items-center gap-4">
            <div className="w-12 h-12 bg-gradient-to-br from-[var(--color-brand-primary)] to-[var(--color-brand-secondary)] rounded-full flex items-center justify-center">
              <FaRobot className="text-white text-2xl" />
            </div>
            <div>
              <h2 className="text-white font-bold text-lg">PredictAI Bot</h2>
              <p className="text-slate-400 text-sm flex items-center gap-2">
                <span className="w-2 h-2 rounded-full bg-green-500 inline-block"></span> Online
              </p>
            </div>
          </div>

          {/* Messages Area */}
          <div className="flex-grow p-6 overflow-y-auto bg-slate-50 space-y-6 custom-scrollbar">
            {messages.map((msg) => (
              <motion.div 
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                key={msg.id} 
                className={`flex gap-4 ${msg.sender === 'user' ? 'justify-end' : 'justify-start'}`}
              >
                {msg.sender === 'bot' && (
                  <div className="w-8 h-8 rounded-full bg-[var(--color-brand-primary)] flex items-center justify-center shrink-0 mt-1">
                    <FaRobot className="text-white text-sm" />
                  </div>
                )}
                
                <div className={`max-w-[75%] px-5 py-3 rounded-2xl ${
                  msg.sender === 'user' 
                    ? 'bg-gradient-to-r from-[var(--color-brand-primary)] to-[var(--color-brand-secondary)] text-white rounded-tr-sm shadow-md' 
                    : 'bg-white border border-slate-200 text-slate-800 rounded-tl-sm shadow-sm'
                }`}>
                  <p className="whitespace-pre-wrap leading-relaxed" dangerouslySetInnerHTML={{ __html: msg.text.replace(/\n/g, '<br/>') }}></p>
                </div>

                {msg.sender === 'user' && (
                  <div className="w-8 h-8 rounded-full bg-slate-200 flex items-center justify-center shrink-0 mt-1">
                    <FaUserCircle className="text-slate-500 text-xl" />
                  </div>
                )}
              </motion.div>
            ))}
            
            {loading && (
              <div className="flex gap-4 justify-start">
                <div className="w-8 h-8 rounded-full bg-[var(--color-brand-primary)] flex items-center justify-center shrink-0 mt-1">
                  <FaRobot className="text-white text-sm" />
                </div>
                <div className="bg-white border border-slate-200 px-5 py-4 rounded-2xl rounded-tl-sm shadow-sm flex gap-2 items-center">
                  <div className="w-2 h-2 bg-slate-400 rounded-full animate-bounce"></div>
                  <div className="w-2 h-2 bg-slate-400 rounded-full animate-bounce" style={{ animationDelay: '0.2s' }}></div>
                  <div className="w-2 h-2 bg-slate-400 rounded-full animate-bounce" style={{ animationDelay: '0.4s' }}></div>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>

          {/* Input Area */}
          <div className="p-4 bg-white border-t border-slate-100">
            <form onSubmit={handleSubmit} className="flex gap-3">
              <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Type your message here..."
                className="flex-grow px-5 py-3 bg-slate-50 border border-slate-200 rounded-full focus:outline-none focus:ring-2 focus:ring-[var(--color-brand-primary)] focus:bg-white transition-colors"
              />
              <button
                type="submit"
                disabled={!input.trim() || loading}
                className="w-12 h-12 shrink-0 bg-gradient-to-r from-[var(--color-brand-primary)] to-[var(--color-brand-secondary)] rounded-full flex items-center justify-center text-white shadow-md hover:shadow-lg disabled:opacity-50 transition-all hover:-translate-y-0.5"
              >
                <FaPaperPlane className="ml-1" />
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ChatbotPage;

import React, { createContext, useState, useEffect } from 'react';
import api from '../api/axios';
import { toast } from 'react-hot-toast';

export const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const initAuth = async () => {
      const tokens = localStorage.getItem('auth_tokens');
      if (tokens) {
        try {
          const res = await api.get('/auth/user/');
          setUser(res.data);
        } catch (error) {
          console.error("Failed to fetch user on load", error);
          localStorage.removeItem('auth_tokens');
        }
      }
      setLoading(false);
    };

    initAuth();
  }, []);

  const login = async (username, password) => {
    try {
      const res = await api.post('/auth/login/', { username, password });
      localStorage.setItem('auth_tokens', JSON.stringify(res.data.tokens));
      setUser(res.data.user);
      return { success: true };
    } catch (error) {
      return { 
        success: false, 
        error: error.response?.data?.error || 'Login failed. Please check your credentials.' 
      };
    }
  };

  const register = async (userData) => {
    try {
      const res = await api.post('/auth/register/', userData);
      localStorage.setItem('auth_tokens', JSON.stringify(res.data.tokens));
      setUser(res.data.user);
      return { success: true };
    } catch (error) {
      return { 
        success: false, 
        error: error.response?.data || { general: ['Registration failed.'] } 
      };
    }
  };

  const logout = async () => {
    try {
      const tokens = localStorage.getItem('auth_tokens');
      if (tokens) {
        const parsedTokens = JSON.parse(tokens);
        await api.post('/auth/logout/', { refresh: parsedTokens.refresh });
      }
    } catch (error) {
      console.error("Logout error", error);
    } finally {
      localStorage.removeItem('auth_tokens');
      setUser(null);
      window.location.href = '/login';
    }
  };

  const updateProfile = async (formData) => {
    try {
      const res = await api.put('/profile/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setUser(res.data);
      return { success: true };
    } catch (error) {
      return { 
        success: false, 
        error: error.response?.data || 'Failed to update profile' 
      };
    }
  };

  const contextValue = {
    user,
    loading,
    login,
    register,
    logout,
    updateProfile,
  };

  return (
    <AuthContext.Provider value={contextValue}>
      {children}
    </AuthContext.Provider>
  );
};

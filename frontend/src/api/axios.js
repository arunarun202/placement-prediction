import axios from 'axios';

const api = axios.create({
  baseURL: '/api',
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor to add the access token to headers
api.interceptors.request.use(
  (config) => {
    const tokens = localStorage.getItem('auth_tokens');
    if (tokens) {
      const parsedTokens = JSON.parse(tokens);
      config.headers.Authorization = `Bearer ${parsedTokens.access}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Response interceptor to handle token refresh
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    // If the error status is 401 and there is no originalRequest._retry flag,
    // it means the token has expired and we need to refresh it
    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      const tokens = localStorage.getItem('auth_tokens');

      if (tokens) {
        const parsedTokens = JSON.parse(tokens);
        try {
          const response = await axios.post('/api/auth/refresh/', {
            refresh: parsedTokens.refresh,
          });

          // Store the new tokens
          const newTokens = {
            ...parsedTokens,
            access: response.data.access,
          };
          localStorage.setItem('auth_tokens', JSON.stringify(newTokens));

          // Update the authorization header for the original request
          api.defaults.headers.common['Authorization'] = `Bearer ${newTokens.access}`;
          originalRequest.headers['Authorization'] = `Bearer ${newTokens.access}`;

          // Retry the original request
          return api(originalRequest);
        } catch (refreshError) {
          // If refresh fails, log out
          localStorage.removeItem('auth_tokens');
          window.location.href = '/login';
          return Promise.reject(refreshError);
        }
      }
    }
    return Promise.reject(error);
  }
);

export default api;

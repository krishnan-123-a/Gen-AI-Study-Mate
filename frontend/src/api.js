import axios from 'axios';

// In production set VITE_API_URL env var to your backend URL.
// In dev, Vite's proxy forwards /api/* → localhost:5000
const BASE_URL = import.meta.env.VITE_API_URL || '';

const api = axios.create({
  baseURL: BASE_URL,
  headers: { 'Content-Type': 'application/json' },
});

export default api;

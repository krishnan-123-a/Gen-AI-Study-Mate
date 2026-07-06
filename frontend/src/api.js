import axios from 'axios';

// In production (Render/Vercel), use the deployed backend URL.
// In development, the proxy in package.json handles /api/* → localhost:5000
const BASE_URL = process.env.REACT_APP_API_URL || '';

const api = axios.create({
  baseURL: BASE_URL,
  headers: { 'Content-Type': 'application/json' },
});

export default api;

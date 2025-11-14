import axios from 'axios';

// creating an instance of Axios   
const api = axios.create({
    baseURL: import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000/api',
    // add headers or interceptors here later for JWT
});

export default api;
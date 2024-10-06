// src/services/api.ts
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/', // Update this with your Django server URL
});

export const registerUser = (data: { username: string; email: string; password: string }) =>
  api.post('/register/', data);

export const loginUser = (data: { username: string; password: string }) =>
  api.post('/login/', data);

export const fetchItems = () => api.get('/items/');
export const createItem = (data: { name: string; description: string }) =>
  api.post('/items/', data);

// Add the uploadImage function here
export const uploadImage = (formData: FormData) =>
  api.post('/convert-image/', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });

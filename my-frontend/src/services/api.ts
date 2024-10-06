// src/services/api.ts
import axios from 'axios';

// Create an instance of axios with the base URL pointing to the Django backend
const api = axios.create({
  baseURL: 'http://localhost:8000/', // Make sure this is the correct Django server URL
});

// Function to set authorization headers with the token from local storage
const setAuthHeader = () => {
  const token = localStorage.getItem('token');
  if (token) {
    return { headers: { Authorization: `Token ${token}` } }; // Use 'Token' as in your curl command
  }
  return {};
};

// Fetch the list of items
export const fetchItems = () => 
  api.get('/items/', setAuthHeader()); // Include authorization header

// Create a new item
export const createItem = (data: { name: string; description: string }) => 
  api.post('/items/', data, setAuthHeader()); // Include authorization header



// Register a new user
export const registerUser = (data: { username: string; email: string; password: string }) => 
  api.post('/register/', data);

// Login an existing user
export const loginUser = (data: { username: string; password: string }) => 
  api.post('/login/', data);


// Upload an image for processing
export const uploadImage = (formData: FormData) => 
  api.post('/convert-image/', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
      ...setAuthHeader().headers, // Include authorization header
    },
  });

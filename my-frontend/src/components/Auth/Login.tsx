// src/components/Auth/Login.tsx
import React, { useState } from 'react';
import { loginUser } from '../../services/api';
import { toast } from 'react-toastify'; // Import toast

const Login: React.FC = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await loginUser({ username, password });
      console.log('User logged in:', response.data);
      toast.success('Login successful!'); // Show success toast
      // Store the token if needed
    } catch (error) {
      console.error('Error logging in:', error);
      toast.error('Failed to log in. Please try again.'); // Show error toast
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        placeholder="Username"
        required
      />
      <input
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Password"
        required
      />
      <button type="submit">Login</button>
    </form>
  );
};

export default Login;

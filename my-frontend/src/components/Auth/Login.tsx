import React, { useState } from 'react';
import { loginUser } from '../../services/api';
import { toast } from 'react-toastify';

const Login: React.FC = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await loginUser({ username, password });
      const { token } = response.data;
      console.log('User logged in:', token);
      toast.success('Login successful!');
      localStorage.setItem('token', token); // Store the token
      // You can redirect the user after login or show the logout button in the navbar
    } catch (error) {
      console.error('Error logging in:', error);
      toast.error('Failed to log in. Please try again.');
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

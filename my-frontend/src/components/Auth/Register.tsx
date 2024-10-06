// src/components/Auth/Register.tsx
import React, { useState } from 'react';
import { registerUser } from '../../services/api';
import { toast } from 'react-toastify'; // Import toast

const Register: React.FC = () => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await registerUser({ username, email, password });
      console.log('User registered:', response.data);
      toast.success('Registration successful!'); // Show success toast
    } catch (error) {
      console.error('Error registering user:', error);
      toast.error('Failed to register. Please try again.'); // Show error toast
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
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="Email"
        required
      />
      <input
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Password"
        required
      />
      <button type="submit">Register</button>
    </form>
  );
};

export default Register;

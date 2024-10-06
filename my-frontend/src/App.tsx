// src/App.tsx
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { ToastContainer } from 'react-toastify'; // Import ToastContainer
import 'react-toastify/dist/ReactToastify.css'; // Import Toastify styles
import ItemList from './components/Items/ItemList';
import ItemForm from './components/Items/ItemForm';
import Register from './components/Auth/Register';
import Login from './components/Auth/Login';
import ImageProcessing from './components/ImageProcessing';
import Navbar from './components/Navbar';
import 'bootstrap/dist/css/bootstrap.min.css';

const App: React.FC = () => {
  return (
    <Router>
      <Navbar />
      <div className="container mt-4">
        <Routes>
          <Route path="/" element={<h1>Home Page</h1>} />
          <Route path="/items" element={<ItemList />} />
          <Route path="/add-item" element={<ItemForm />} />
          <Route path="/register" element={<Register />} />
          <Route path="/login" element={<Login />} />
          <Route path="/image-processing" element={<ImageProcessing />} />
        </Routes>
      </div>
      <ToastContainer /> {/* Include the ToastContainer to render toasts */}
    </Router>
  );
};

export default App;

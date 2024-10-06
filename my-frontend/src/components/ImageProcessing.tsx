// src/components/ImageProcessing.tsx
import React, { useState } from 'react';
import { uploadImage } from '../services/api'; // You will need to implement this API endpoint

const ImageProcessing: React.FC = () => {
  const [image, setImage] = useState<File | null>(null);

  const handleImageChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) {
      setImage(e.target.files[0]);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (image) {
      const formData = new FormData();
      formData.append('input_image_path', image);
      // Call your image processing API here
      try {
        const response = await uploadImage(formData);
        console.log('Image processed:', response.data);
      } catch (error) {
        console.error('Error processing image:', error);
      }
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="file" onChange={handleImageChange} required />
      <button type="submit">Process Image</button>
    </form>
  );
};

export default ImageProcessing;

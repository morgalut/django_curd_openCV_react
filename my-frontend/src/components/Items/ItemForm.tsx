// src/components/Items/ItemForm.tsx
import React, { useState } from 'react';
import { createItem } from '../../services/api';

const ItemForm: React.FC = () => {
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await createItem({ name, description });
      console.log('Item created:', response.data);
      // Optionally reset form fields
      setName('');
      setDescription('');
    } catch (error) {
      console.error('Error creating item:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Item Name"
        required
      />
      <textarea
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        placeholder="Item Description"
        required
      />
      <button type="submit">Create Item</button>
    </form>
  );
};

export default ItemForm;

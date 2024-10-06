// src/components/Items/Items.tsx
import React, { useEffect, useState } from 'react';
import { fetchItems } from '../../services/api';
import { Navigate } from 'react-router-dom';

interface Item {
  id: number;
  name: string;
  description: string;
}

const ItemList: React.FC = () => {
  const [items, setItems] = useState<Item[]>([]);
  const token = localStorage.getItem('token'); // Make sure the token is saved properly in local storage

  useEffect(() => {
    const getItems = async () => {
      try {
        const response = await fetchItems();
        setItems(response.data);
      } catch (error) {
        console.error('Error fetching items:', error);
      }
    };
    getItems();
  }, []);

  if (!token) {
    return <Navigate to="/login" />;
  }

  return (
    <ul>
      {items.map((item) => (
        <li key={item.id}>
          <h3>{item.name}</h3>
          <p>{item.description}</p>
        </li>
      ))}
    </ul>
  );
};

export default ItemList;

// src/components/Items/ItemList.tsx
import React, { useEffect, useState } from 'react';
import { fetchItems } from '../../services/api';

interface Item {
  id: number;
  name: string;
  description: string;
}

const ItemList: React.FC = () => {
  const [items, setItems] = useState<Item[]>([]);

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

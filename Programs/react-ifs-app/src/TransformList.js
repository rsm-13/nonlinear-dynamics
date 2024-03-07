import React from 'react';
import './App.css'; // Import the CSS file

const TransformList = ({ transforms, onEdit, onDelete }) => {
  const handleEdit = (transform, index) => {
    onEdit(transform, index); // Call the onEdit function passed from the parent component
  };

  return (
    <div className="transform-list">
      <h3>Transforms</h3>
      <ul>
        {transforms.map((transform, index) => (
          <li key={index}>
            <span>{`Transform ${index + 1}: `}</span>
            <button className='transform-btn' onClick={() => handleEdit(transform, index)}>✎</button>
            <button className='transform-btn' onClick={() => onDelete(index)}>⌫</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TransformList;
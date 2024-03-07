import React, { useState } from 'react';
import './App.css';

const ColorChooser = ({ label, onChange }) => {
  const [color, setColor] = useState('#000000'); // Initial color state

  const handleChange = (e) => {
    setColor(e.target.value);
    onChange(e.target.value)
  };

  return (
    <div className="color-chooser">
      <label>{label}: </label>
      <input type="color" value={color} onChange={handleChange} />

    </div>
  );
};

export default ColorChooser;

import React, { useState } from 'react';
import './App.css'; // Import the CSS file
import ColorChooser from './ColorChooser';
import FractalGenerator from './FractalGenerator';

const ControlPanel = ({ onAbout, onAddTransform }) => {
  // State variables to track the values of the sliders
  const [transients, setTransients] = useState(50);
  const [iterations, setIterations] = useState(50);

  // Event handler for transients slider change
  const handleTransientsChange = (e) => {
    const newTransients = parseInt(e.target.value);
    setTransients(newTransients);
    FractalGenerator.getInstance().setTransients(newTransients);
  };

  // Event handler for iterations slider change
  const handleIterationsChange = (e) => {
    const newIterations = parseInt(e.target.value);
    setIterations(newIterations);
    FractalGenerator.getInstance().setIterations(newIterations);
  };

  return (
    <div className="control-panel">
      <button className="button" onClick={()=> window.open("https://docs.google.com/document/d/17OlPo_UHvbIP0QBQzymwkfms4aY2zuGoR3LAo_7dRYk/edit?usp=sharing", "_blank")}>About</button>
      <button className="button" onClick={onAddTransform}>Add Transform</button>
      <br /><br />
      <div>
        <label>Transients:</label>
        <input type="range" min="0" max="500000" value={transients} onChange={handleTransientsChange} />
        <span>{transients}</span> {/* Display current value */}
      </div>
      <div>
        <label>Iterations:</label>
        <input type="range" min="0" max="5000000" value={iterations} onChange={handleIterationsChange} />
        <span>{iterations}</span> {/* Display current value */}
      </div>
      <br />
      <ColorChooser label="Background Color" onChange={(newColor)=>{
        FractalGenerator.getInstance().setBgColor(newColor)
        console.log(newColor)
      }} /> {/* Add color chooser for background color */}
      <br />
      <button className="button" onClick={()=>{FractalGenerator.getInstance().generate()}}>Update</button>
      <br />
    </div>
  );
};

export default ControlPanel;

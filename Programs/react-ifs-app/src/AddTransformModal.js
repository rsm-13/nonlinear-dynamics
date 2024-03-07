import React, { useState, useEffect } from 'react';
import FractalGenerator from './FractalGenerator';
import IFS_Transform from './IFS_Transform';

const AddTransformModal = ({ onSubmit, onClose, editTransform, trsIndex, isEdit }) => {
  const [xScale, setXScale] = useState(1.0);
  const [yScale, setYScale] = useState(1.0);
  const [theta, setTheta] = useState(0.0);
  const [phi, setPhi] = useState(0.0);
  const [p, setP] = useState(0.0);
  const [h, setH] = useState(0.0);
  const [k, setK] = useState(0.0);
  const [color, setColor] = useState('#000000');

  useEffect(() => {
    if (editTransform) {
      setXScale((editTransform.xScale));
      setYScale((editTransform.yScale));
      setTheta((editTransform.theta));
      setPhi((editTransform.phi));
      setP((editTransform.p));
      setH((editTransform.h));
      setK((editTransform.k));
      setColor((editTransform.color));
    }
  }, [editTransform]);

  const handleSubmit = (e) => {
    e.preventDefault();
    const newTransform = new IFS_Transform(
      xScale,
      yScale,
      theta,
      phi,
      p,
      h,
      k,
      color
    );
    onSubmit(newTransform); // Pass the new transformation data to the onSubmit function
    FractalGenerator.getInstance().addTransformationToIFS(newTransform, isEdit, trsIndex); //
    onClose(); // Close the modal after submission
  };

  return (
    <div className="modal-overlay">
      <div className="add-transform-modal">
        <h2>{editTransform ? 'Edit Transform' : 'Add Transform'}</h2>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>x-Scale:</label>
            <input type="number" step="0.01" value={xScale} onChange={(e) => setXScale(parseFloat(e.target.value))} />
          </div>
          <div className="form-group">
            <label>y-Scale:</label>
            <input type="number" step="0.01" value={yScale} onChange={(e) => setYScale(parseFloat(e.target.value))} />
          </div>
          <div className="form-group">
            <label>Theta (θ):</label>
            <input type="number" step="0.01" value={theta} onChange={(e) => setTheta(parseFloat(e.target.value))} />
          </div>
          <div className="form-group">
            <label>Phi (Φ):</label>
            <input type="number" step="0.01" value={phi} onChange={(e) => setPhi(parseFloat(e.target.value))} />
          </div>
          <div className="form-group">
            <label>Probability:</label>
            <input type="number" step="0.01" value={p} onChange={(e) => setP(parseFloat(e.target.value))} />
          </div>
          <div className="form-group">
            <label>h:</label>
            <input type="number" step="0.01" value={h} onChange={(e) => setH(parseFloat(e.target.value))} />
          </div>
          <div className="form-group">
            <label>k:</label>
            <input type="number" step="0.01"  value={k} onChange={(e) => setK(parseFloat(e.target.value))} />
          </div>
          <div className="form-group">
            <label>Color:</label>
            <input type="color" value={color} onChange={(e) => setColor(e.target.value)} />
          </div>
          <div className="form-group">
            <button type="submit">{editTransform ? 'Update' : 'Done'}</button>
            <button type="button" onClick={onClose}>Cancel</button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default AddTransformModal;

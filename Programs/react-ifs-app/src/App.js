import React, { useState } from 'react';
import ControlPanel from './ControlPanel';
import TransformList from './TransformList';
import AddTransformModal from './AddTransformModal';
import FractalGenerator from './FractalGenerator'; // Import the FractalGenerator component
import './App.css'; // Import the CSS file
import FractalComponent from './FractalComponent';
import IFS_Transform from './IFS_Transform';

const defaultTransforms = [
  new IFS_Transform(0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 1, 'brown'),
  new IFS_Transform(0.5, 0.5, -35, 0.0, 0.5, 0.0, 1, 'blue'),
  new IFS_Transform(0.5, 0.5, 35, 0.0, -0.5, 0.0, 1, 'purple')
]

const App = () => {
  // State variables for managing transforms and other UI states
  const [zoom, setZoom] = useState(1);
  const [transforms, setTransforms] = useState(defaultTransforms);
  const [showAddTransformModal, setShowAddTransformModal] = useState(false);
  const [selectedTransform, setSelectedTransform] = useState(null);
  const [selectedIdx, setSelectedIdx] = useState(0);
  const [isEdit, setIsEdit] = useState(false);
  const [transients, setTransients] = useState(0); // Initial value of 0
  const [iterations, setIterations] = useState(0); // Initial value of 0
  const [bgColor, setBgColor] = useState('#ffffff'); // Initial value of white

  // Function to add a new transform
  const addTransform = (newTransform) => {
    setTransforms([...transforms, newTransform]);
    setShowAddTransformModal(false); // Close the modal after adding transform
    setSelectedTransform(null); // Reset selectedTransform
  };

  // Function to delete a transform
  const deleteTransform = (index) => {
    FractalGenerator.getInstance().deleteTransform(index);
    let newTransforms = [...transforms];
    newTransforms.splice(index, 1);
    setTransforms(newTransforms);
  };

  // Function to edit a transform
  const editTransform = (updatedTransform) => {
    const index = transforms.indexOf(selectedTransform);
    if (index !== -1) {
      const updatedTransforms = [...transforms];
      updatedTransforms[index] = updatedTransform;
      setTransforms(updatedTransforms);
      setShowAddTransformModal(false); // Close the modal after editing transform
      setSelectedTransform(null); // Reset selectedTransform
    }
  };

  const updateFractal = () => {
    FractalGenerator.getInstance().setTransients(transients);
    FractalGenerator.getInstance().setIterations(iterations);
    FractalGenerator.getInstance().setBgColor(bgColor);
  };

  //FractalGenerator.getInstance().setDefaultTransforms(transforms);


  return (
    <div className="app">
      <header>
        <h1><center>Iterated Function System Explorer</center></h1>
        <br></br>
      </header>
      <div className="main-container">
        <div className="fractal-display">
          <br></br>
          <FractalComponent transforms={transforms}/>
        </div>
        <div className="control-panel">
          <br></br>
          <div className="cp-container">
            <h3>Control Panel</h3>
            <ControlPanel
              onAbout= {() => {}}
              onAddTransform={() => {
                setIsEdit(false);
                setShowAddTransformModal(true);
                setSelectedTransform(null); // Reset selectedTransform when adding new transform
              }}
              onZoomIn={() => FractalComponent.updateZoom(true)}
              onZoomOut={() => FractalComponent.updateZoom(false)}

            />
          </div>
          <TransformList
            transforms={transforms}
            onEdit={(transform, index) => {
              setIsEdit(true);
              setSelectedTransform(transform); // Set the selected transform for editing
              setSelectedIdx(index)
              setShowAddTransformModal(true); // Open the add transform modal
            }}
            onDelete={deleteTransform}
          />
        </div>
      </div>
      {showAddTransformModal && (
        <AddTransformModal
          onSubmit={selectedTransform ? editTransform : addTransform} // Choose between edit or add based on selectedTransform
          onClose={() => {
            setShowAddTransformModal(false);
            setSelectedTransform(null); // Reset selectedTransform when closing the modal
          }}
          editTransform={selectedTransform} // Pass selectedTransform to the modal for editing
          trsIndex={selectedIdx}
          isEdit={isEdit}
        />
      )}
    </div>
  );
};

export default App;

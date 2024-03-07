import React, { useEffect, useRef, useState } from 'react';
import FractalGenerator from './FractalGenerator';

function FractalComponent({ zoom: initialZoom, transforms, setBgColor, setTransients, setIterations}) {
    const canvasRef = useRef(null);
    const [zoom, setZoom] = useState(initialZoom);
    const [fractalGenerator, setFractalGenerator] = useState(null);

    const updateZoom = (isZoomIn) => {
        let newZoom = isZoomIn ? zoom * 1.5 : zoom / 1.5;
        setZoom(newZoom);
        if (fractalGenerator) {
            fractalGenerator.zoom(isZoomIn);
            fractalGenerator.generate();
        }
    };

    useEffect(() => {
        const canvas = canvasRef.current;
        const generator = FractalGenerator.getInstance(canvas, transforms);
        setFractalGenerator(generator);
        generator.zoom(zoom);
        generator.generate();
    }, [zoom]);

    return (
        <div>
            <canvas ref={canvasRef} width={600} height={600}></canvas>
            <br />
            <button className="button2" onClick={() => updateZoom(true)}>Zoom In</button>
            <button className="button2" onClick={() => updateZoom(false)}>Zoom Out</button>
        </div>
    );
}

export default FractalComponent;
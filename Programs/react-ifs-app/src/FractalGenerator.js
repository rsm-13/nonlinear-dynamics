import IFS_Transform from './IFS_Transform';
import { random, randrange } from './random';

class FractalGenerator {
  static myInstance = null;

  constructor(canvas, transforms) {
    this.canvas = canvas;
    this.bg = 'white';
    this.ctx = canvas.getContext('2d');
    this.IFS = [];

    //for (let transform in transforms) {
    this.addTransformationToIFS(new IFS_Transform(0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 1, 'brown'),true,0)
    this.addTransformationToIFS(new IFS_Transform(0.5, 0.5, -35, 0.0, 0.5, 0, 1, 'blue'),true,1)
    this.addTransformationToIFS(new IFS_Transform(0.5, 0.5, 35, 0.0, -0.5, 0, 1, 'purple'),true,2)
    //this.addTransformationToIFS(new IFS_Transform(0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 1, 'black'), true, 0)
    //this.addTransformationToIFS(new IFS_Transform(0.5, 0.5, 0.0, 0.0, 0.5, 0.0, 1, 'blue'), true, 1)
    //this.addTransformationToIFS(new IFS_Transform(0.5, 0.5, 0.0, 0.0, 0.25, 0.5, 1, 'green'), true, 2)
    //}

    //this.IFS.push(new IFS_Transform(0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 1, 'black'));
    //this.IFS.push(new IFS_Transform(0.5, 0.5, 0.0, 0.0, 0.5, 0.0, 1, 'blue'));
    //this.IFS.push(new IFS_Transform(0.5, 0.5, 0.0, 0.0, 0.25, 0.5, 1, 'green'));

    this.pt = [canvas.width / 0.5, canvas.height / 0.5];
    this.transients = 500000;
    this.iters = 5000000;
    this.zoomFactor = 1;
    this.centerX = 0;
    this.centerY = 0;

    // Add a click event listener to the canvas
    canvas.addEventListener('click', this.handleCanvasClick.bind(this));
  }

  static getInstance() {
    return this.myInstance;
  }

  static getInstance(canvas, transforms) {
    if(FractalGenerator.myInstance == null) {
      FractalGenerator.myInstance = new FractalGenerator(canvas, transforms);
    }
    return this.myInstance;
  }
    
  addTransformationToIFS(transform, edit, idx) {
    if (edit === true) {
      this.IFS[idx] = transform;
    } else {
      this.IFS.push(transform)
    }
    console.log(this.IFS)
    console.log(edit)
    console.log(idx)
    this.generate()
  }

  deleteTransform(idx) {
    this.IFS.splice(idx,1)
    console.log(this.IFS)
    console.log(idx)
    this.generate()
  }

  setBgColor(color) {
    this.bg = color;
    //this.ctx.fillStyle = color;
  }

  setTransients(transients) {
    this.transients = transients;
  }

  setIterations(iters) {
    this.iters = iters;
  }


  handleCanvasClick(event) {
    const rect = this.canvas.getBoundingClientRect();
    const x = (event.clientX - rect.left) / (rect.right - rect.left);
    const y = (event.clientY - rect.top) / (rect.bottom - rect.top);
  
    // Transform the clicked point from the canvas's coordinate system to the fractal's coordinate system
    const fractalX = (x - 0.33) / this.zoomFactor + this.centerX;
    const fractalY = ((y * this.canvas.height / this.canvas.width) - 0.33) / this.zoomFactor + this.centerY;

    this.centerX = fractalX;
    this.centerY = fractalY;

    this.generate();
  }

  plot(x, y, color) {
    const canvasWidth = this.canvas.width;
    const canvasHeight = this.canvas.height;

    // Adjust the points to be relative to the center
    const centeredX = (x - this.centerX) * this.zoomFactor;
    const centeredY = (y - this.centerY) * this.zoomFactor;

    const scaledX = centeredX * (canvasWidth / 1.5);
    const scaledY = centeredY * (canvasHeight / 1.5);

    const offsetX = canvasWidth / 3.5;
    const offsetY = canvasHeight / 3.5;

    this.ctx.fillStyle = color;
    this.ctx.fillRect(scaledX + offsetX, scaledY + offsetY, 0.09, 0.09);
  }

  drawOutline() {
    this.ctx.strokeStyle = 'black';
    this.ctx.lineWidth = 2;
    this.ctx.strokeRect(0, 0, this.canvas.width, this.canvas.height);
  }

  generate() {
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    this.ctx.fillStyle = this.bg
    this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

    if (this.IFS.length  === 0) return;

    for (let n = 0; n < this.transients; n++) {
      const t = this.IFS[randrange(this.IFS.length)];
      this.pt = t.transformPoint(this.pt);
    }

    for (let n = 0; n < this.iters; n++) {
      const t = this.IFS[randrange(this.IFS.length)];
      this.pt = t.transformPoint(this.pt);
      this.plot(this.pt[0], this.pt[1], t.getColor());
    }

    this.drawOutline();
  }

  zoom(isZoomIn) {
    if (isZoomIn) {
      this.zoomFactor *= 1.5;
    } else {
      this.zoomFactor /= 1.5;
    }
  }
}

export default FractalGenerator;

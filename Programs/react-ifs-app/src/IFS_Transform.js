class IFS_Transform {
    constructor(xScale = 0.5, yScale = 0.5, theta = 0.0, phi = 0.0, h = 0.0, k = 0.0, p = 1, c = 'white') {
        this.r = xScale;
        this.s = yScale;
        this.theta = theta;
        this.phi = phi;
        this.thetaRadians = this.toRadians(this.theta);
        this.phiRadians = this.toRadians(this.phi);
        this.e = h;
        this.f = k;
        this.prob = p;
        this.color = c;
    }

    toRadians(angle) {
        return angle * (Math.PI / 180);
    }

    setR(xScale) {
        this.r = xScale;
    }

    setS(yScale) {
        this.s = yScale;
    }

    setTheta(angle) {
        this.theta = angle;
        this.thetaRadians = this.toRadians(this.theta);
    }

    setPhi(angle) {
        this.phi = angle;
        this.phiRadians = this.toRadians(this.phi);
    }

    setHshift(shift) {
        this.e = shift;
    }

    setVshift(shift) {
        this.f = shift;
    }

    setProb(prob) {
        this.prob = prob;
    }

    setColor(myColor) {
        this.color = myColor;
    }

    getR() {
        return this.r;
    }

    getS() {
        return this.s;
    }

    getTheta() {
        return this.theta;
    }

    getPhi() {
        return this.phi;
    }

    getE() {
        return this.e;
    }

    getF() {
        return this.f;
    }

    getProb() {
        return this.prob;
    }

    getColor() {
        return this.color;
    }

    transformPoint(pt) {
        const newX = pt[0] * this.r * Math.cos(this.thetaRadians) - pt[1] * this.s * Math.sin(this.phiRadians) + this.e;
        const newY = pt[0] * this.r * Math.sin(this.thetaRadians) + pt[1] * this.s * Math.cos(this.phiRadians) + this.f;
        return [newX, newY];
    }

    toString() {
        return `[scale(${this.r},${this.s}), rot(${this.theta},${this.phi}), trans(${this.e},${this.f}), prob(${this.prob}), col(${this.color})]`;
    }
}

export default IFS_Transform
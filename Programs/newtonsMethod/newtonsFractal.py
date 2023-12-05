# Author: Radha Munver
# Date: 12/06/2023
# (AT) Nonlinear Dynamics
# Fractal Class (Polynomial_Newtons) for Newton's Method Explorer

# IMPORTS --------------------------
import sys
sys.path.append("../util")

import cmath as cm
import numpy as np
from DEgraphics_Radha import *
from colorTheory import ColorTheory
from random import shuffle


# FRACTAL CLASS --------------------

class Polynomial_Newtons(ColorTheory):
    
    def __init__(self, window=None, degree=3):
        super().__init__()  # call the constructor of parent class (ColorTheory)

        if window != None:
            self.window = window
        
        else:
            self.window = DEGraphWin(width=500, height=500, hasTitlebar=False, autoflush=False, hBGColor=None, hThickness=0)
        self.window.setBackground('#464b4f')
        
        # set base attributes
        self.PAL_newtons = self.getRandomPal()
        self.deg = degree
        self.res = 0.03
        self.mag = 'high'
        self.iters = 50
        self.ratio = 1

        self.drawFract()
        
    # draw the fractal on the window
    def drawFract(self):
        degree = self.deg  # use the desired degree of the polynomial
        coefficients = self.generate_poly_coefficients(degree)
        
        global roots
        roots = np.roots(coefficients)  # calculate complex roots

        self.window.clear()
        self.iterateAll(coefficients)

    # change the degree of the polynomial
    def changeDegree(self, degree):
        self.deg = degree

    # update the zoom ratio based on the zoom count (num times zoomed in)
    # uses exponential increase to make sure zoom is still visible
    def updateRatio(self, ratio, zoomCount):
        self.ratio *= (ratio**zoomCount) * 0.2

    # change the resolution threshold
    def changeRes(self, res):
        if res == 'high':
            self.mag = 'high'
            self.res = 0.03 * self.ratio
        elif res == 'med':
            self.mag = 'med'
            self.res = 0.04 * self.ratio
        elif res == 'low':
            self.mag = 'low'
            self.res = 0.05 * self.ratio

    # evaluate the polynomial function at a given point
    def f(self, z, coefficients):
        result = 0
        for i, coeff in enumerate(coefficients[::-1]):
            result += coeff * z**i
        return result

    # evaluate the derivative of the polynomial function at a given point
    def df(self, z, coefficients):
        result = 0
        for i, coeff in enumerate(coefficients[:-1][::-1]):
            result += (i + 1) * coeff * z**i
        return result

    # apply newton's method to find roots of the polynomial
    def newtons(self, z, coefficients):
        f_value = self.f(z, coefficients)
        df_value = self.df(z, coefficients)
        
        # Set a threshold for magnitude to avoid division by zero
        threshold = 1e-10
        
        if abs(df_value) < threshold:
            # If magnitude is below the threshold, use a small value instead
            adjusted_df = threshold
        else:
            # Otherwise, use the original derivative
            adjusted_df = df_value
        
        return z - (f_value / adjusted_df)

    #Iterate Newton's method for a given starting point.
    def iterate(self, z0, coefficients):
        n = self.iters
        for i in range(n):
            z0 = self.newtons(z0, coefficients)
        return z0

    #Iterate Newton's method for all points in the window and plot the colors.
    def iterateAll(self, coefficients):
        global roots
        roots = np.roots(coefficients)
        factor = self.res

        real_values = np.arange(self.window.currentCoords[0], self.window.currentCoords[2], factor)
        imag_values = np.arange(self.window.currentCoords[1], self.window.currentCoords[3], factor)

        # create a 2D array to store the colors
        colors = np.empty((len(real_values), len(imag_values)), dtype=object)

        # iterate over each point and store the color in the array
        for i, real in enumerate(real_values):
            for j, imag in enumerate(imag_values):
                z = complex(real, imag)
                z = self.iterate(z, coefficients)
                color = self.getColor(z, roots)
                colors[i, j] = color

        # draw the entire array at once
        for i, real in enumerate(real_values):
            for j, imag in enumerate(imag_values):
                self.window.plot(real, imag, colors[i, j])

        self.window.update()

    # change the number of iterations for Newton's method
    def changeIters(self, n):
        self.iters = int(n)

    # generate coefficients for a polynomial of given degree.
    def generate_poly_coefficients(self, degree):
        coefficients = [1] + [0] * (degree - 1) + [-1]
        return coefficients
        

def main():
    g = Polynomial_Newtons()
    g.window.getMouse()
    g.window.close()

if __name__ == "__main__":
    main()

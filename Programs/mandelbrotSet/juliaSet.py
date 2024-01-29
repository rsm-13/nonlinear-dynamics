# Author: Radha Munver
# Date: 1/30/2023
# (AT) Nonlinear Dynamics
# Julia Set Class (JuliaSet) for Super Mandelbrot Explorer


# IMPORTS ---------------------------
import sys
sys.path.append("../util")
from DEgraphics_Radha import *
import numpy as np
import time as time
import math
from random import random


# JULIA SET CLASS -------------------
class JuliaSet:

    def __init__(self, pixelWidth, pixelHeight):
        self.win = DEGraphWin(title="Julia Set", width=pixelWidth, height=pixelHeight, defCoords=[-2, -2, 2, 2], offsets=[676, 85], hasTitlebar=False, hBGColor='white', hThickness=0)
        self.win.setBackground('black')
        self.maxIterates = 250  # Max # of iterations for Julia set algorithm


    def escapePlotSet(self, const=0.365 - 0.37j, maxIters=250):
        # Escape / exterior algorithm for plotting of Julia set
        start = time.time()

        # Creating a grid of complex numbers within the current window coordinates
        self.maxIterates = maxIters
        y, x = np.ogrid[self.win.currentCoords[1]:self.win.currentCoords[3]:self.win.height*1j, self.win.currentCoords[0]:self.win.currentCoords[2]:self.win.width*1j]
        c = x + y * 1j
        z = c
        divIter = self.maxIterates + np.zeros(z.shape, dtype=int)

        # Iterating through Julia set escape algorithm
        for i in range(self.maxIterates):
            z = z**2 + const
            diverge = abs(z) >= 2
            divCurr = diverge & (divIter == self.maxIterates)
            divIter[divCurr] = i
            z[diverge] = 2

        # Plotting points based on the iteration count
        for i in range(len(c)):
            for ii in range(len(c[i])):
                iters = divIter[i][ii]
                if iters != self.maxIterates:
                    z = c[i][ii]
                    color = iters * 2
                    if color > 255:
                        color = 255
                    self.win.plot(z.real, z.imag, color_rgb(color, color, color))

        self.win.update()
        print(f"Julia High-Quality Runtime = {round(time.time()-start,3)} sec, for c-Val: {const}")


    def inversePlotSet(self, const=0.365 - 0.37j):
            # Inverse plotting of the Julia set using a random initial complex number
            def g(z, c=const):
                i = 1
                if random() < 0.5:
                    i = -1
                return i * (z - c) ** 0.5

            start = time.time()
            z = complex(-3 + 3 * random(), -3 + 3 * random())

            # Iterating through the inverse Julia set algorithm
            for i in range(10000):
                z = g(z)

            # Plotting points based on the inverse Julia set algorithm
            for i in range(5000):
                z = g(z)
                self.win.plot(z.real, z.imag, 'white')

            self.win.update()
            print(f"Julia Low-Quality Runtime = {round(time.time()-start,3)} sec, for c-Val: {const}")


    def zoom(self, inout="in", iterates=250, fill=False, constant=0.365 - 0.37j, algo='Escape'):
        # Zooming into or out of the Julia set and re-plotting
        self.win.zoom(winControl=self.win, whichWay=inout)
        if algo == 'Escape':
            self.escapePlotSet(const=constant, maxIters=iterates)
        if algo == 'Inverse':
            self.inversePlotSet(const=constant)


    def clear(self):
        self.win.clear()


if __name__ == '__main__':
    m = JuliaSet(800, 800)
    
    # Default: inverse algorithm
    m.inversePlotSet()
    m.win.getMouse()
    m.win.close()


# TESTING C-VALUES
'''
0
1j
-1j
-0.123 + 0.745j
-0.77 + 0.22j
0.365 - 0.37j
-0.8 + 0.156j
-0.835 - 0.2321j
-0.4 + 0.6j
0.279
'''
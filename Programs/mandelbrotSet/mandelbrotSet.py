# Author: Radha Munver
# Date: 1/30/2023
# (AT) Nonlinear Dynamics
# Mandelbrot Set Class (MandelbrotSet) for Super Mandelbrot Explorer

# IMPORTS ------------------------
import sys
sys.path.append("../util")

from DEgraphics_Radha import *
import numpy as np
import time as time


# MANDELBROT CLASS ---------------
class MandelbrotSet:

    def __init__ (self, pixelWidth, pixelHeight):
        self.window = DEGraphWin(title="Mandelbrot Set", width=pixelWidth, height=pixelHeight, defCoords = [-2.1,-1.4,0.8,1.4], offsets=[226,85], hasTitlebar=False, hBGColor='white', hThickness=0)
        self.window.setBackground('black')
        self.maxIterates = 50
        self.color1 = None
        self.color2 = None
        self.single = None

    def escapePlotSet(self, maxIters=250, start_color=(0,0,255), end_color=(0,0,0), single='1T:Blue', twoTone=False):
        # Regular plotting of the Mandelbrot set using the current window coordinates
        start = time.time()
        self.maxIterates = maxIters
        y, x = np.ogrid[self.window.currentCoords[1]:self.window.currentCoords[3]:self.window.height*1j, self.window.currentCoords[0]:self.window.currentCoords[2]:self.window.width*1j]
        c = x + y*1j
        z = c
        divIter = self.maxIterates + np.zeros(z.shape, dtype=int)

        # Iterating through the Mandelbrot set algorithm
        for i in range(self.maxIterates):
            z = z**2 + c
            diverge = abs(z) >= 2
            divCurr = diverge & (divIter == self.maxIterates)
            divIter[divCurr] = i
            z[diverge] = 2

        
        # Plotting points based on iteration count
        for i in range(len(c)):
            for ii in range(len(c[i])):
                iters = divIter[i][ii]
                if iters != self.maxIterates:
                    z = c[i][ii]
                    
                    # TWO TONE GRADIENT --------------
                    if twoTone:
                        self.color1 = start_color
                        self.color2 = end_color
                        if iters <= 40:
                            red_component = int((iters / 40) * (self.color2[0] - self.color1[0]) + self.color1[0])
                            green_component = int((iters / 40) * (self.color2[1] - self.color1[1]) + self.color1[1])
                            blue_component = int((iters / 40) * (self.color2[2] - self.color1[2]) + self.color1[2])
                        else:
                            red_component = int(((self.maxIterates - iters) / (self.maxIterates - 40)) * (self.color1[0] - self.color2[0]) + self.color2[0])
                            green_component = int(((self.maxIterates - iters) / (self.maxIterates - 40)) * (self.color1[1] - self.color2[1]) + self.color2[1])
                            blue_component = int(((self.maxIterates - iters) / (self.maxIterates - 40)) * (self.color1[2] - self.color2[2]) + self.color2[2])
                        
                        # Plot the point with the calculated color
                        self.window.plot(z.real, z.imag, color_rgb(red_component, green_component, blue_component))
                    
                    
                    # SINGLE TONE GRADIENT --------------
                    if not twoTone:
                        self.single = single
                        if iters <= 40:
                            color = iters * 6 + 50
                            if color > 255:
                                color = 255
                            if single == '1T:Red':
                                self.window.plot(z.real, z.imag, color_rgb(color, 0, 0))
                            elif single == '1T:Green':
                                self.window.plot(z.real, z.imag, color_rgb(0, color, 0))
                            elif single == '1T:Blue':
                                self.window.plot(z.real, z.imag, color_rgb(0, 0, color))
                            
                        else:
                            color = 255 - iters * 3
                            if color < 0:
                                color = 1
                                self.window.plot(z.real, z.imag, color_rgb(color, color * 10, 0))


        self.window.update()
        print(f"Mandelbrot Runtime = {round(time.time()-start,3)} sec")


    def zoom(self, inout='in',iterates=250,tones=True):
        self.window.zoom(winControl=self.window, whichWay=inout)
        self.escapePlotSet(maxIters=iterates, start_color=self.color1, end_color=self.color2, single=self.single, twoTone=tones)


    def clear(self):
        self.window.clear()



if __name__ == "__main__":
    m = MandelbrotSet(800, 800)

    m.escapePlotSet()
    m.zoom()

    m.window.getMouse()
    m.window.close()

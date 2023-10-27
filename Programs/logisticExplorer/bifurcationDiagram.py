# Author: Radha Munver
# Date: 10/26/2023
# (AT) Nonlinear Dynamics
# Bifurcation Diagram Class for Logistic Map Explorer

from DEgraphics_Radha import *
from math import *
from random import random

class BifurcationDiagram:

    def __init__ (self, window=None):

        def logisticMap(x,r):
            return r * x * (1.0 - x)
        self.function = logisticMap

        # init window settings and draw bif diagram
        coords=[-0.335,-0.2,4,1]
        self.window = window
        self.coords = coords
        self.window.setCoords(self.coords[0],self.coords[1],self.coords[2],self.coords[3])
        self.displayUnitLabels_X()
        self.displayUnitLabels_Y()

        self.drawBifurcationDiagram()


    def drawBifurcationDiagram(self, numTrans = 5000, numIters = 500):
        # for each R-value
        #   generate a random starting value x0 in (0,1)
        #   iterate from x0 a number of transient iterations WITHOUT plotting
        #   iterate the regular iterations and plot each point at (r,x0)

        # clear window make sure axes shown
        self.window.clear()
        if not self.window.axesDrawn:
            self.window.toggleAxes()

        rmin = self.window.currentCoords[0]
        rmax = self.window.currentCoords[2]
        rstep = (rmax - rmin) / self.window.width
        r = rmin
        
        while r < rmax:
            x0 = random()   # 0 <= x0 < 1.0

            # iterate away the transient
            for n in range(numTrans):
                x0 = self.function(x0,r)

            # iterate and plot
            for n in range(numIters):
                x0 = self.function(x0,r)
                self.window.plot(r, x0, '#0672c9')

            r += rstep  #increment

        self.window.update()
    

    def fetch_R(self):
        # Get r-val from point on bifurcation diagram & return its x-val
        ptR = self.window.getMouse()
        r = round(ptR.getX(), 3)
        return r


    def displayUnitLabels_X(self):
        # draw horizontal-axis tick marks and labels
        for r_tick in range(1, 5):
            r_val = r_tick
            self.window.plot(r_val, -0.005, 'black')  # tick mark
            r_label = Text(Point(r_val, -0.05), str(r_val)+'.0', 'times new roman', 'black', 10)
            r_label.setStyle('italic')
            r_label.draw(self.window)
        
        self.r_Axis = Text(Point(2, -0.15), "R", 'times new roman', 'black', 12)
        self.r_Axis.setStyle('italic')
        self.r_Axis.draw(self.window)


    def displayUnitLabels_Y(self):
        # draw vertical-axis tick marks and labels
        for x_tick in range(1, 11):
            x_val = x_tick / 10
            self.window.plot(-0.005, x_val, 'black')  # tick mark
            x_label = Text(Point(-0.1, x_val), str(x_val), 'times new roman', 'black', 10)
            x_label.setStyle('italic')
            x_label.draw(self.window)


def main():
    g = BifurcationDiagram()
    while True:
        g.window.getMouse()
    g.window.close()

if __name__ == "__main__":
    main()

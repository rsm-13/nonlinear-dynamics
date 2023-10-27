# Author: Radha Munver
# Date: 10/26/2023
# (AT) Nonlinear Dynamics
# Time-Series Plot Class for Logistic Map Explorer

# IMPORTS ----------------------
import sys
sys.path.append("../util")

from DEgraphics_Radha import *
from random import random

class TimeSeriesPlot:
    global lines
    lines=[]

    def __init__ (self, window=None):
        self.window = window
        self.r = 1.1
        self.plotTimeSeries(r=1.1, x0=0.3, numIters=30, numTrans=0)
        self.window.setCoords(-0.7,-0.27,5.5,1.5)
        

    def logisticMap(self, x, r):
        return r * x * (1.0 - x)

    
    def plotTimeSeries(self, r, x0, numTrans, numIters):

        # clear canvas
        self.window.clear()
        self.clearTimeSeries()
        
        # horizontal-axis label (t for time)
        self.timeAxis = Text(Point(2.75, -0.13), "t", 'times new roman', 'black', 14)
        self.timeAxis.setStyle('italic')
        self.timeAxis.draw(self.window)
        self.displayUnitLabels_X(1.0)

        # vertical-axis label (x_t)
        self.vertAxis = Text(Point(-0.45, 0.7), "x_t", 'times new roman', 'black', 12)
        self.vertAxis.setStyle('italic')
        self.vertAxis.draw(self.window)
        self.displayUnitLabels_Y(0.2)
        
        # make sure axes are shown
        if not self.window.axesDrawn:
            self.window.toggleAxes()

        if x0 is None:
            # pick random x-val
            x = random()
        else:   # use given initial x-val
            x = x0

        # calculate the x-scale based on the canvas width (5.25) (to ensure always fit in window view)
        x_scale = 5.25 / numIters

        # start i at far left of win & increment to the right while plotting
        i = 0
        while i < numTrans:
            x = self.logisticMap(x, r)
            i += 1
        i = 0   # reset i & x for steady-state phase

        # PLOTTING ALL ITERATIONS
        while i < numIters:
            nextX = self.logisticMap(x, r)  # get next x-val
            
            # use dots if more than 100 iters
            if numIters > 100:
                self.window.plot(x, nextX, '#0672c9')

            # lines if fewer than 100 iters
            else:
                # draw line from i, x to the next i, f(x)
                line = Line(Point(i * x_scale, x), Point((i + 1) * x_scale, nextX), style='solid')
                line.setFill('#0672c9')
                line.draw(self.window)

            # append it to lines
            # increment
            lines.append(line)
            x = nextX
            i += 1


    # set new R-val
    def setR(self, R):
        self.r = R


    def displayUnitLabels_X(self, interval):
        # draw horizontal-axis tickmarks and units
        for x in range(1, 6):
            x_value = x * interval
            x_value_str = "{:.1f}".format(x_value)  # format to one decimal place
            unitLabel = Text(Point(x_value, -0.04), x_value_str, 'times new roman', 'black', 8)
            unitLabel.setStyle('italic')
            unitLabel.draw(self.window)


    def displayUnitLabels_Y(self, interval):
        # draw vertical-axis tickmarks and units
        for y in range(1, 6):
            y_value = y * interval
            y_value_str = "{:.1f}".format(y_value)  # format to one decimal place
            unitLabel = Text(Point(-0.15, y_value), y_value_str, 'times new roman', 'black', 8)
            unitLabel.setStyle('italic')
            unitLabel.draw(self.window)


    def clearTimeSeries(self):
        # undraw / erase all lines in time series to properly clear
        # clear "lines" list & then clear windo
        for line in lines:
            line.undraw()
        
        lines.clear()
        self.window.clear()

        
def main():
    g = TimeSeriesPlot()
    g.window.getMouse()
    g.window.close()

if __name__ == "__main__":
    main()
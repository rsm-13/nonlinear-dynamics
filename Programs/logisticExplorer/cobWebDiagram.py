# Author: Radha Munver
# Date: 10/26/2023
# (AT) Nonlinear Dynamics
# Cobweb Diagram Class for Logistic Map Explorer

# IMPORTS ----------------------
import sys
sys.path.append("../util")
from DEgraphics_Radha import *

class CobwebDiagram:

    #initialize the cobweb object
    def __init__ (self, flush=True, window=None):
        
        def logisticMap(x,r):
            return (r * x) * (1.0 - x)
        
        self.function = logisticMap
        self.window = window
        self.flushing = flush
        self.r = 1.1
        self.x0 = 0.3

        self.window.setCoords(-0.2, -0.2, 1.1, 1.1)

        # horizontal-axis label (x_t)
        self.xt_Axis = Text(Point(0.525,-0.1),"x_t",'times new roman','black',13)
        self.xt_Axis.setStyle('italic')
        self.xt_Axis.draw(self.window)

        # vertical-axis label (x_(t+1))
        self.xt1_Axis = Text(Point(-0.14,0.52), "x_\n(t+1)",'times new roman','black',10)
        self.xt1_Axis.setStyle('italic')
        self.xt1_Axis.draw(self.window)

        # draw axis tickmarks and units
        self.displayUnitLabels_X()
        self.displayUnitLabels_Y()

        # steady-state line
        steadyStateLine = Line(Point(0, 0), Point(1, 1))
        steadyStateLine.draw(self.window)

        self.drawCobwebDiagram()


    def drawCobwebDiagram(self, numIters = 10, numTrans = 0):
        self.window.clear()

        # make sure axes shown
        if not self.window.axesDrawn:
            self.window.toggleAxes()

        # init x and r vals
        x0 = self.x0
        r = self.r

        # compute & skip transient iters
        for _ in range(numTrans):
            x0 = self.function(x0, r)

        # draw parabola for cobweb
        x = 0
        while x <= 1:
            self.window.plot(x, self.function(x,r), 'black')
            x += 0.0005
        self.window.update()

        # plot the steady-state behavior
        
        # starting vals
        x_prev = x0
        y_prev = 0
        
        # moving_x signifies whether to move line horizontally or vertically
        # True = vertically | False  = horizontally
        moving_x = False    

        # plot for all iters
        for _ in range(numIters):
            if moving_x:
                moving_x = False
                target_y = y_prev

                # Move horizontally
                if x_prev < target_y:
                    while x_prev < target_y:
                        self.window.plot(x_prev, y_prev, '#0672c9')
                        x_prev += 0.001
                else:
                    while x_prev > target_y:
                        self.window.plot(x_prev, y_prev, '#0672c9')
                        x_prev -= 0.001
            else:
                moving_x = True
                target_y = self.function(x_prev, r)

                # Move vertically
                if y_prev < target_y:
                    while y_prev < target_y:
                        self.window.plot(x_prev, y_prev, '#0672c9')
                        y_prev += 0.001
                else:
                    while y_prev > target_y:
                        self.window.plot(x_prev, y_prev, '#0672c9')
                        y_prev -= 0.001

        self.window.update()


    # set r & x val attributes for cobweb
    def setRX(self, r, x):
        self.r = r
        self.x0 = x

    
    def displayUnitLabels_X(self):
        # draw horizontal-axis tickmarks and units
        for x in range(1, 11):
            x_value = x / 10.0
            self.window.plot(x_value, 0, 'black')
            unitLabel = Text(Point(x_value, -0.035), str(x / 10), 'times new roman', 'black', 8)
            unitLabel.setStyle('italic')
            unitLabel.draw(self.window)


    def displayUnitLabels_Y(self):
        # Draw vertical-axis tickmarks and units
        for y in range(1, 11):
            y_value = y / 10.0
            self.window.plot(0, y_value, 'black')
            unitLabel = Text(Point(-0.05, y_value), str(y / 10), 'times new roman', 'black', 8)
            unitLabel.setStyle('italic')
            unitLabel.draw(self.window)


def main():
    g = CobwebDiagram()
    g.drawCobwebDiagram()
    g.window.getMouse()
    g.window.close()

if __name__ == "__main__":
    main()
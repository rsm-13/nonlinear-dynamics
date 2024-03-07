import sys
sys.path.append("../util")

from transform import IFS_Transform
from DEgraphics import *
from random import random, randrange

def main():
    win = DEGraphWin(width = 800, height = 800, offsets = [150,100], defCoords=[-0.1, -0.1, 1.1, 1.1], hasTitlebar=False)

    IFS = []

    #IFS.append(IFS_Transform(xScale = 0.5, yScale = 0.5, theta = 0.0, phi = 0.0,
    #                        h = 0.0, k = 0.0, p = 1, c = 'black'))
    
    #IFS.append(IFS_Transform(xScale = 0.5, yScale = 0.5, theta = 0.0, phi = 0.0,
    #                        h = 0.5, k = 0.0, p = 1, c = 'red'))
    
    #IFS.append(IFS_Transform(xScale = 0.5, yScale = 0.5, theta = 0.0, phi = 0.0,
    #                        h = 0.25, k = 0.5, p = 1, c = 'green'))
    IFS.append(IFS_Transform(xScale = 0.5, yScale = 0.5, theta = 0.0, phi = 0.0, h = 0.0, k = 0.0, p = 1, c = 'brown'))
    IFS.append(IFS_Transform(xScale = 0.5, yScale = 0.5, theta = -30, phi = 0.0, h = 0.5, k = 0.0, p = 1, c = 'brown'))
    IFS.append(IFS_Transform(xScale = 0.5, yScale = 0.5, theta = 30, phi = 0.0, h = -0.5, k = 0.0, p = 1, c = 'brown'))



    win.getMouse()

    pt = (100*random(), 100*random())
    transients = 10000
    iters = 100000

    #transient loop
    for n in range(transients):
        # randomly choose a transform
        t = IFS[randrange(len(IFS))]
        pt = t.transformPoint(pt)

    #iters loop & draw
    for n in range(iters):
        
        t = IFS[randrange(len(IFS))]
        pt = t.transformPoint(pt)
        win.plot(pt[0], pt[1], t.getColor())

    win.getMouse()
    win.close()

main()
#if __name__ == 'main':
    #main()
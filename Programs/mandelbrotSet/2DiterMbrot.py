import sys
sys.path.append("../util")

from DEgraphics import *
import cmath as cm
from random import random as rnd

def f(z,c):
    return z*z + c

def main():

    # the Mandelbrot Set is named after Benoit Mandelbrot
    # and is based upon the one-parameter family of quadratic maps
    # F(z) = z^2 + c

    # Definitions:
    #   1. The Mset is the set of all c-values for which the orbit of 0 under f(z) remains bounded
    #   2. The Mset is the set of all c-values for which the associated Julia Set of z^2 + c is a connected set
    #      (if the c-val is NOT in the MSet, then the associated Jset is TOTALLY disconnected!
    #       These pathological Jsets are said to be comprised of "center dust.")
    #       
    win = DEGraphWin(width = 600, height = 600, defCoords=[-2,5,-1.5,0.5,1.5])
    win.toggleAxes()

    win.getMouse()

    maxSize = 5
    maxIters = 50
    real = -2.5

    while real < 0.5:
        imag = -1.5

        while imag < 1.5:
            c = complex(real, imag)
            z = complex(0,0)
            iters = 0
            while iters < maxIters and abs(z) < maxSize:
                z = f(z,c)
                iters += 1

            if iters == maxIters:
                win.plot(real, imag)
            imag += 0.01

        real += 0.01
        win.update()
    
    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()
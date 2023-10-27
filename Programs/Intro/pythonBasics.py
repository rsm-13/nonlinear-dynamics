#intro to basics in python, much of which
# should be review for students in NLD...

# set up the ability to see another folder
import sys
sys.path.append("../util")

# import the graphics library from the util folder
# import sine function
from DEgraphics import *
from math import sin

# define a main method
def main():
    # demonstrate use of print statements here
    print("Hello World!")
    print("Whoops! I meant", end = ' ')
    print("Hello Universe!")

    # create a graphing window
    winPlot = DEGraphWin(title = "My First NLD Graphics Program",
    	         defCoords=[-8,-6,8,6], margin = [0,0],
                 axisType = 0, axisColor = 'black',
                 width = 800, height = 600,
                 offsets=[200,100], autoflush = False,
                 hasTitlebar = True,
                 hThickness=2, hBGColor="blue",
                 borderWidth=0)
    #winPlot.setBackground('white')
    axisColor = 'black'
    winPlot.toggleAxes()

    # graph y = sin(x) on winPlot in red
    x = -8
    count = 0
    while x < 3:
        winPlot.plot(x, 4 * sin(x), 'red')  # .plot() takes 3 inputs
        x += 0.001
        count += 1

        if count % 1000 == 0:
            winPlot.update()


    # wait for a click, then close the window
    winPlot.getMouse()
    winPlot.close()

# if running main, then start main,
# otherwise just import to use methods without running main
if __name__ == "__main__":
    main()
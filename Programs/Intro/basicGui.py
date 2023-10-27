# a basic gui with 3 windows

# set up the ability to see another folder
import sys
sys.path.append("../util")

from DEgraphics import *

def main():
    # custom coordinate settings
    xmin = -12
    xmax = 12
    ymin = -4
    ymax = 4

    # list to contain all windows
    myWindows = []

    winA = DEGraphWin(title = "winA", width = 600, height = 230,
                      defCoords = [xmin,ymin,xmax,ymax],
                      offsets = [200,100], autoflush = False,
                      hasTitlebar = False)
    winA.setBackground("white")
    winA.toggleAxes()
    myWindows.append(winA)

    winCP = DEGraphWin(title = "control panel", width = 200, height = 200,
                       defCoords = [0,0,20,20], offsets = [800,100])
    myWindows.append(winCP)

    winExplanation = DEGraphWin(width = 600, height = 50,
                                offsets = [200,330],
                                hasTitlebar = False)
    winExplanation.setBackground("red")
    myWindows.append(winExplanation)

    winBtmRight = DEGraphWin(width = 200, height = 50,
                                offsets = [800,330],
                                hasTitlebar = False)
    winBtmRight.setBackground("green")
    myWindows.append(winBtmRight)

    btnZoom = Button(winCP, topLeft = Point(12,19), width=3, height=3,
                    edgeWidth=2, label='2',
                    buttonColors=['blue','black','black'],
                    clickedColors=['white','red','black'],
                    font=('courier',18), timeDelay=0.25)
    btnZoom.activate()

    btnExit = Button(winCP, topLeft = Point(16,19), width=3, height=3,
                 edgeWidth = 2, label = 'X',
                 buttonColors = ['red','black','black'],
                 clickedColors = ['white','red','black'],
                 font=('courier',18), timeDelay = 0.25)
    btnExit.activate()

    clickPt = winCP.getMouse()
    while not btnExit.clicked(clickPt):
        clickPt = winCP.getMouse()
        if btnZoom.clicked(clickPt):
            winA.zoom('in')

    for window in myWindows:
        window.close()


if __name__ == "__main__":
    main()
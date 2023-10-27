# Author: Radha Munver
# Date: 10/9/2023
# Uses DEGraphics written by J. Iwanski
# A basic gui with 4 windows
# -----------------------------------------------------------------

# set up the ability to see another folder
import sys
sys.path.append("../util")

from DEgraphics import *

def main(x,y):
    # custom coordinate settings
    defCoords = [-12,-4,12,4]

    # list to contain all windows
    myWindows = []

    # ---------------------- RED WINDOW ---------------------------

    winA = DEGraphWin(title = "winA", width = 602, height = 50,
                      defCoords = defCoords,
                      offsets = [x,y], autoflush = False,
                      hasTitlebar = False, hThickness=0, hBGColor='black')
    winA.setBackground("#d46363")
    myWindows.append(winA)

    #create & style header text
    txtWinA = Text(Point(0,0),'Layout Number 3')
    txtWinA.setTextColor('black')
    txtWinA.setFace('courier')
    txtWinA.setSize(14)
    txtWinA.draw(winA)

    # ---------------------- BLUE WINDOW ---------------------------

    winB = DEGraphWin(width = 200, height = 200,
                                offsets = [x,y+52],
                                hasTitlebar = False, hThickness=0, hBGColor='black')
    winB.setBackground("#8eaebd")
    myWindows.append(winB)

    #add image of piet painting
    here = os.path.dirname(os.path.abspath(__file__))
    image = Image(Point(0,0), here+"/img/piet_rby.png")
    image.draw(winB)    


    # ---------------------- GREEN WINDOW ---------------------------

    winC = DEGraphWin(width = 400, height = 200,
                                offsets = [x+202,y+52],
                                hasTitlebar = False, hThickness=0, hBGColor='black')
    winC.setBackground("#809e82")
    myWindows.append(winC)

    #create & style fact text
    fact = '\
            Dutch, Neoplasticism artist,\n\
            Piet Mondrian, is famous for\n\
            his 1930 painting, “Composition\n\
            with Red Blue and Yellow,”\n\
            which views similar to this\n\
            GUI layout due to his defining\n\
            borders around colored rectangles.\n\
            See his piece to the left.'

    txtWinC = Text(Point(-2,0),fact)
    txtWinC.setTextColor('black')
    txtWinC.setFace('courier')
    txtWinC.setSize(12)
    txtWinC.draw(winC)


    # ---------------------- YELLOW WINDOW ---------------------------

    winD = DEGraphWin(width = 602, height = 50,
                                offsets = [x,y+254],
                                hasTitlebar = False, hThickness=0, hBGColor='black')
    winD.setBackground("#ebc17f")
    myWindows.append(winD)

    # change background color button for red window
    btnBGColor = Button(winD, topLeft = Point(-6,2), width=5, height=7,
                 edgeWidth = 2, label = 'Change winA BG Color',
                 buttonColors = ['white','black','black'],
                 clickedColors = ['#e38484','red','black'],
                 font=('courier', 12, 'italic'), timeDelay = 0.2)
    btnBGColor.activate()

    # move GUI 10 right
    btnRGUI = Button(winD, topLeft = Point(1.5,2), width=1, height=7,
                 edgeWidth = 2, label = '>',
                 buttonColors = ['white','black','black'],
                 clickedColors = ['#e38484','red','black'],
                 font=('courier', 12, 'italic'), timeDelay = 0.2)
    btnRGUI.activate()

    # move GUI 10 left
    btnLGUI = Button(winD, topLeft = Point(0,2), width=1, height=7,
                 edgeWidth = 2, label = '<',
                 buttonColors = ['white','black','black'],
                 clickedColors = ['#e38484','red','black'],
                 font=('courier', 12, 'italic'), timeDelay = 0.2)
    btnLGUI.activate()

    # close windows button
    btnExit = Button(winD, topLeft = Point(-9,2), width=2, height=7,
                 edgeWidth = 2, label = 'close',
                 buttonColors = ['#d95252','#ad3939','#fce3e3'],
                 clickedColors = ['#e38484','red','black'],
                 font=('courier', 12, 'italic'), timeDelay = 0.2)
    btnExit.activate()


    clickPt = winD.getMouse()   #check what was clicked
    currBG = 0  #state of winA color (0: red, 1: purple)

    while not btnExit.clicked(clickPt):     #perform clicks while not exited
        
        clickPt = winD.getMouse()

        if btnBGColor.clicked(clickPt):
            if currBG == 0:
                winA.setBackground("#ad9dc4")   #change to purple
                currBG = 1

            elif currBG == 1:
                winA.setBackground("#d46363")   #change to red
                currBG = 0
        
        #close windows and move GUI 10px to the RIGHT
        if btnRGUI.clicked(clickPt):
            for window in myWindows:
                window.close()
            
            main(x+10,y)
        
        #close windows and move GUI 10px to the LEFT
        if btnLGUI.clicked(clickPt):
            for window in myWindows:
                window.close()
            
            main(x-10,y)

    for window in myWindows:
        window.close()


if __name__ == "__main__":
    main(200,100)   #input starting position
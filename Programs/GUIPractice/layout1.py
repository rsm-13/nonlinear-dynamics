# Author: Radha Munver
# Date: 10/9/2023
# Uses DEGraphics written by J. Iwanski
# A basic gui with 5 windows
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
    txtWinA = Text(Point(0,0),'Layout Number 1')
    txtWinA.setTextColor('black')
    txtWinA.setFace('courier')
    txtWinA.setSize(14)
    txtWinA.draw(winA)


    # ---------------------- BLUE WINDOW ---------------------------

    winB = DEGraphWin(width = 250, height = 300,
                                offsets = [x,y+52],
                                hasTitlebar = False, hThickness=0, hBGColor='black')
    winB.setBackground("#8eaebd")
    myWindows.append(winB)


    fact = '\
            Instructions:\n\n\
            the "close" button \n\
            will close all windows.\n\n\
            the button to its right \n\
            will toggle the background\n\
            color of the header from red\n\
            to purple.\n\n\
            the "<" button will move\n\
            the GUI 10px to the LEFT.\n\n\
            the ">" button will move\n\
            the GUI 10px to the RIGHT.'

    #create & style instructions text
    txtWinB = Text(Point(-3.5,0),fact)
    txtWinB.setTextColor('black')
    txtWinB.setFace('courier')
    txtWinB.setSize(12)
    txtWinB.draw(winB)


    # ---------------------- GREEN WINDOW ---------------------------

    winC = DEGraphWin(width = 250, height = 200,
                                offsets = [x+252,y+52],
                                hasTitlebar = False, hThickness=0, hBGColor='black')
    winC.setBackground("#809e82")
    myWindows.append(winC)

    txtAbout = '\
            Uses: DEGraphics.py\n\n\
            Graphics Library Written by:\n\
            Mr. Joseph Iwanski'
    
    #create & style About text
    txtWinC = Text(Point(-3,0),txtAbout)
    txtWinC.setTextColor('black')
    txtWinC.setFace('courier')
    txtWinC.setSize(12)
    txtWinC.draw(winC)


    # ---------------------- BLACK WINDOW ---------------------------

    winD = DEGraphWin(width = 98, height = 200,
                                offsets = [x+504,y+52],
                                hasTitlebar = False, hThickness=0, hBGColor='black')
    winD.setBackground('#2e2d2d')
    myWindows.append(winC)

    txtDetails = '\
            Author:\n\
            Radha\n\
            Munver\n\n\
            Date:\n\
            10/9/2023'

    #create & style header text
    txtWinD = Text(Point(-8,0),txtDetails)
    txtWinD.setTextColor('white')
    txtWinD.setFace('courier')
    txtWinD.setSize(12)
    txtWinD.draw(winD)


    # ---------------------- YELLOW WINDOW ---------------------------

    winE = DEGraphWin(width = 350, height = 98,
                                offsets = [x+252,y+254],
                                hasTitlebar = False, hThickness=0, hBGColor='black')
    winE.setBackground("#ebc17f")
    myWindows.append(winE)

    # change background color button for red window
    btnBGColor = Button(winE, topLeft = Point(-4.75,2), width=9, height=6,
                 edgeWidth = 2, label = 'Change winA BG Color',
                 buttonColors = ['white','black','black'],
                 clickedColors = ['#e38484','red','black'],
                 font=('courier', 12, 'italic'), timeDelay = 0.2)
    btnBGColor.activate()

    # move GUI 10 right
    btnRGUI = Button(winE, topLeft = Point(7.5,2), width=2, height=6,
                 edgeWidth = 2, label = '>',
                 buttonColors = ['white','black','black'],
                 clickedColors = ['#e38484','red','black'],
                 font=('courier', 12, 'italic'), timeDelay = 0.2)
    btnRGUI.activate()

    # move GUI 10 left
    btnLGUI = Button(winE, topLeft = Point(5,2), width=2, height=6,
                 edgeWidth = 2, label = '<',
                 buttonColors = ['white','black','black'],
                 clickedColors = ['#e38484','red','black'],
                 font=('courier', 12, 'italic'), timeDelay = 0.2)
    btnLGUI.activate()

    # close windows button
    btnExit = Button(winE, topLeft = Point(-9,2), width=3.5, height=6,
                 edgeWidth = 2, label = 'close',
                 buttonColors = ['#d95252','#ad3939','#fce3e3'],
                 clickedColors = ['#e38484','red','black'],
                 font=('courier', 12, 'italic'), timeDelay = 0.2)
    btnExit.activate()


    clickPt = winE.getMouse()
    currBG = 0  #state of interface mode (0: dark, 1: light)

    while not btnExit.clicked(clickPt):     #perform clicks
        
        clickPt = winE.getMouse()

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
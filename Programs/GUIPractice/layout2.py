# Author: Radha Munver
# Date: 10/9/2023
# Uses DEGraphics written by J. Iwanski
# A basic gui with 6 windows
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

    #create & style the header text
    txtWinA = Text(Point(0,0),'Layout Number 2')
    txtWinA.setTextColor('black')
    txtWinA.setFace('courier')
    txtWinA.setSize(14)
    txtWinA.draw(winA)


    # ---------------------- BLUE WINDOW ---------------------------

    winB = DEGraphWin(width = 225, height = 300,
                                offsets = [x,y+52],
                                hasTitlebar = False, hThickness=0, hBGColor='black')
    winB.setBackground("#8eaebd")
    myWindows.append(winB)

    #create & style fact text
    fact = '\
            The two images displayed\n\
            are the works of\n\
            M.C. Escher. To the right\n\
            is "Double Planetoid," a\n\
            3D fractal-like piece.\n\
            His works as a whole\n\
            incorporate geometry &\n\
            artistry, but are reminders\n\
            of the nonuniformity and\n\
            strange patterns explicit\n\
            in nonlinear dynamics!'

    txtWinE = Text(Point(-3.75,0),fact)
    txtWinE.setTextColor('black')
    txtWinE.setFace('courier')
    txtWinE.setSize(12)
    txtWinE.draw(winB)

    # ---------------------- GREEN WINDOW ---------------------------

    winC = DEGraphWin(width = 225, height = 200,
                                offsets = [x+227,y+52],
                                hasTitlebar = False, hThickness=0, hBGColor='black')
    winC.setBackground("#809e82")
    myWindows.append(winC)

    #add image of high and low painting
    here = os.path.dirname(os.path.abspath(__file__))
    image = Image(Point(0,0), here+"/img/double-planetoid.png")
    image.draw(winC)

    # ---------------------- ORANGE WINDOW ---------------------------

    winD = DEGraphWin(width = 148, height = 400,
                                offsets = [x+454,y+52],
                                hasTitlebar = False, hThickness=0, hBGColor='black')
    winD.setBackground('#f2a17e')
    myWindows.append(winD)

    #add image of high and low painting
    here = os.path.dirname(os.path.abspath(__file__))
    image = Image(Point(0,0), here+"/img/hl-escher.png")
    image.draw(winD)


    # ---------------------- PINK WINDOW ---------------------------

    winE = DEGraphWin(width = 225, height = 98,
                                offsets = [x+227,y+254],
                                hasTitlebar = False, hThickness=0, hBGColor='black')
    winE.setBackground("#ba9baf")
    myWindows.append(winE)

    #create & style fact text
    imgTitle = 'High and Low -->'

    txtWinE = Text(Point(0,0),imgTitle)
    txtWinE.setTextColor('black')
    txtWinE.setFace('courier')
    txtWinE.setSize(14)
    txtWinE.draw(winE)

    # ---------------------- YELLOW WINDOW ---------------------------

    winF = DEGraphWin(width = 452, height = 98,
                                offsets = [x,y+354],
                                hasTitlebar = False, hThickness=0, hBGColor='black')
    winF.setBackground("#ebc17f")
    myWindows.append(winF)

    # change background color button for red window
    btnBGColor = Button(winF, topLeft = Point(-4.75,2), width=9, height=6,
                 edgeWidth = 2, label = 'Change winA BG Color',
                 buttonColors = ['white','black','black'],
                 clickedColors = ['#e38484','red','black'],
                 font=('courier', 12, 'italic'), timeDelay = 0.2)
    btnBGColor.activate()

    # move GUI 10 right
    btnRGUI = Button(winF, topLeft = Point(7.5,2), width=2, height=6,
                 edgeWidth = 2, label = '>',
                 buttonColors = ['white','black','black'],
                 clickedColors = ['#e38484','red','black'],
                 font=('courier', 12, 'italic'), timeDelay = 0.2)
    btnRGUI.activate()

    # move GUI 10 left
    btnLGUI = Button(winF, topLeft = Point(5,2), width=2, height=6,
                 edgeWidth = 2, label = '<',
                 buttonColors = ['white','black','black'],
                 clickedColors = ['#e38484','red','black'],
                 font=('courier', 12, 'italic'), timeDelay = 0.2)
    btnLGUI.activate()

    # close windows button
    btnExit = Button(winF, topLeft = Point(-9,2), width=3.5, height=6,
                 edgeWidth = 2, label = 'close',
                 buttonColors = ['#d95252','#ad3939','#fce3e3'],
                 clickedColors = ['#e38484','red','black'],
                 font=('courier', 12, 'italic'), timeDelay = 0.2)
    btnExit.activate()


    clickPt = winF.getMouse()
    currBG = 0  #state of winA color (0: red, 1: purple)

    while not btnExit.clicked(clickPt):     #perform clicks
        
        clickPt = winF.getMouse()

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
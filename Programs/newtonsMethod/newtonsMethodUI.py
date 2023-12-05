# Author: Radha Munver
# Date: 12/06/2023
# (AT) Nonlinear Dynamics
# UI for Newtons Method Explorer


# IMPORTS ------------------------

import sys
sys.path.append("../util")

from tkinter import *
from DEgraphics_Radha import *
from newtonsFractal import *
from colorTheory import *
import webbrowser
from threading import Thread
import os


# MAIN ---------------------------

def main(x,y):
    
    global dark, light
    dark = '#464b4f'
    light = '#959ca1'
    deg = 0
    iters = 50
    zoomCount = 0

    myWindows = []
    buttons = []

    # -------------------------------- HEADER -----------------------------------

    winHead = DEGraphWin(title = "header", width = 800, height = 60,
                      defCoords = [-12,-4,12,4],
                      offsets = [x,y], autoflush = False,
                      hasTitlebar = False, hThickness=0, hBGColor='black')
    winHead.setBackground("#363637")
    myWindows.append(winHead)

    #create & style header text
    txtHead = Text(Point(0,0),"Newton's Method Explorer", 'times new roman',
                   'white', 14)
    txtHead.setStyle('italic')
    txtHead.draw(winHead)


    # ----------------------------- CONTROL PANEL -------------------------------

    winCP = DEGraphWin(title = "", width = 225, height = 800,
                      offsets = [x,y+55], autoflush = False,
                      hasTitlebar = True, hThickness=0, hBGColor='white')
    winCP.setBackground(dark)
    myWindows.append(winCP)
    

    # hamburger menu
    btnMenu = Button(winCP, topLeft = Point(-7.8,9.5), width=3, height=0.7,
                edgeWidth = 0, label = '☰', radius=0,
                buttonBG = dark, txtColor = 'white',
                clickedBG = dark, clickedTxtColor = '#7362a1',
                font=('avenir', 27, 'bold'), timeDelay = 0.2)

    # about
    btnAbout = Button(winCP, topLeft = Point(-7,8.25), width=14, height=0.7,
                edgeWidth = 1, label = 'About', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#e2daf5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)
    buttons.append(btnAbout)
    
    # change background color button (dark/light mode)
    btnBGColor = Button(winCP, topLeft = Point(-7,7.25), width=14, height=0.7,
                edgeWidth = 1, label = 'Dark / Light Mode', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#e2daf5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)
    buttons.append(btnBGColor)
    
    # fractal zoom-in btn
    btnZmIn = Button(winCP, topLeft = Point(-7,6.25), width=6.5, height=0.7,
                edgeWidth = 1, label = 'Zoom-In', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#e2daf5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)
    buttons.append(btnZmIn)
    
    # fractal zoom-out btn
    btnZmOut = Button(winCP, topLeft = Point(0.5,6.25), width=6.5, height=0.7,
                edgeWidth = 1, label = 'Zoom-Out', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#e2daf5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)
    buttons.append(btnZmOut)
    
    # open color / fractal menu
    btnOpenColorMenu = Button(winCP, topLeft = Point(-7,5.25), width=14, height=0.7,
                edgeWidth = 1, label = 'Color, Res, & Poly Menu', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#e2daf5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)
    buttons.append(btnOpenColorMenu)
    
    # clear fractal win and reset to new default (z^3-1)
    btnClear = Button(winCP, topLeft = Point(-7,4.25), width=14, height=0.7,
                edgeWidth = 1, label = 'Clear', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#e2daf5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)
    buttons.append(btnClear)
    
    # quit program btn
    btnExit = Button(winCP, topLeft = Point(-7,3.25), width=14, height=0.7,
                edgeWidth = 1, label = 'Quit Program', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#e2daf5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)
    buttons.append(btnExit)
    
    btnMenu.activate()
    btnAbout.activate()
    btnZmIn.activate()
    btnZmOut.activate()
    btnOpenColorMenu.activate()
    btnClear.activate()
    btnExit.activate()
    btnBGColor.activate()

    # undraw buttons for closed hamburger menu
    for btn in buttons:
        btn.undraw()

    # author / about
    txtAuthor = Text(Point(3.75,9.05), 'Radha Munver\nDec. 2023', 'avenir', 'white', 9)
    txtAuthor.setStyle('italic')
    txtAuthor.draw(winCP)

    # ------------------------------ SUB-MENU --------------------------------


    txtFractMenu = Text(Point(1.75,1), 'FRACTAL MENU', 'avenir', 'white', 14)
    txtFractMenu.setStyle('italic') 

    txtPal = Text(Point(0,0), 'Palettes', 'avenir', 'white', 12)
    txtRes = Text(Point(0,-4.25), 'Resolution', 'avenir', 'white', 12)
    txtPoly = Text(Point(0,-6.5), 'Polynomial Degree', 'avenir', 'white', 12)

    # INIT BUTTONS ---------------

    btnApplyChanges = Button(winCP, topLeft = Point(-6.75,1.3), width=1.70, height=0.49,
                edgeWidth = 1, label = '☑', radius=0,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#bfe6f5', clickedTxtColor = 'black',
                font=('avenir', 36, 'italic'), timeDelay = 0.2)

    btnShuffle = Button(winCP, topLeft = Point(4.25,0.35), width=2.0, height=0.58,
                edgeWidth = 1, label = '⟳', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#bfe6f5', clickedTxtColor = 'black',
                font=('avenir', 22, 'italic'), timeDelay = 0.2)
    
    btnPalOption1 = Button(winCP, topLeft = Point(-6.8,-0.72), width=1.0, height=0.3,
                edgeWidth = 1, label = '', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#bfe6f5', clickedTxtColor = 'black',
                font=('avenir', 22, 'italic'), timeDelay = 0.2)
    
    btnPalOption2 = Button(winCP, topLeft = Point(-6.8,-1.47), width=1.0, height=0.3,
                edgeWidth = 1, label = '', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#bfe6f5', clickedTxtColor = 'black',
                font=('avenir', 22, 'italic'), timeDelay = 0.2)
    
    btnPalOption3 = Button(winCP, topLeft = Point(-6.8,-2.22), width=1.0, height=0.3,
                edgeWidth = 1, label = '', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#bfe6f5', clickedTxtColor = 'black',
                font=('avenir', 22, 'italic'), timeDelay = 0.2)

    btnHi = Button(winCP, topLeft = Point(-6.5,-4.75), width=4, height=0.7,
                edgeWidth = 1, label = 'High', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#e2daf5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)
    
    btnMed = Button(winCP, topLeft = Point(-2,-4.75), width=4, height=0.7,
                edgeWidth = 1, label = 'Med', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#e2daf5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)
    
    btnLow = Button(winCP, topLeft = Point(2.5,-4.75), width=4, height=0.7,
                edgeWidth = 1, label = 'Low', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#e2daf5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)

    btnPoly_2 = Button(winCP, topLeft = Point(-6.5,-7), width=2.5, height=0.7,
                edgeWidth = 1, label = '2', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#e2daf5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)

    btnPoly_3 = Button(winCP, topLeft = Point(-3,-7), width=2.5, height=0.7,
                edgeWidth = 1, label = '3', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#e2daf5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)
    
    btnPoly_4 = Button(winCP, topLeft = Point(0.5,-7), width=2.5, height=0.7,
                edgeWidth = 1, label = '4', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#e2daf5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)

    btnPoly_5 = Button(winCP, topLeft = Point(4,-7), width=2.5, height=0.7,
                edgeWidth = 1, label = '5', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#e2daf5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)
    
    btnPoly_6 = Button(winCP, topLeft = Point(-6.5,-8), width=2.5, height=0.7,
                edgeWidth = 1, label = '6', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#e2daf5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)

    btnPoly_7 = Button(winCP, topLeft = Point(-3,-8), width=2.5, height=0.7,
                edgeWidth = 1, label = '7', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#e2daf5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)
    
    btnPoly_8 = Button(winCP, topLeft = Point(0.5,-8), width=2.5, height=0.7,
                edgeWidth = 1, label = '8', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#e2daf5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)

    btnPoly_9 = Button(winCP, topLeft = Point(4,-8), width=2.5, height=0.7,
                edgeWidth = 1, label = '9', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#e2daf5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)

    menuOutline = Rectangle(p1=Point(-9,1.75), p2=Point(9,-9.25))
    menuOutline.setOutline('#7362a1')

    
    # PALETTES ---------------------------
    #add images of palette samples
    here = os.path.dirname(os.path.abspath(__file__))
    imgPal0 = Image(Point(1,-0.875), here+"/img/palette0.png")
    imgPal1 = Image(Point(1,-1.625), here+"/img/palette1.png")
    imgPal2 = Image(Point(1,-2.4), here+"/img/palette2.png")

    # ITERS ------------------------------

    txtNumIters = Text(Point(7.5,-3.25),'# Iterations:\t\t\t\t[0,200]', 'times new roman',
                        'white', 12)

    entryNumIters = IntEntry(center=Point(4.5,-3.25), width=5, span = [0,200],
                            colors=['white','black'],
                            errorColors=['red','white'])
    entryNumIters.setDefault(50)
    entryNumIters.setText(iters)
    entryNumIters.draw(winCP)
    txtNumIters.draw(winCP)

    # ELEMENTS ---------------------------

    subMenu = [txtFractMenu, txtPal, txtRes, txtPoly, \
                imgPal0, imgPal1, imgPal2, \
                entryNumIters, txtNumIters, \
                btnPalOption1, btnPalOption2, btnPalOption3, \
                btnShuffle, btnHi, btnMed, btnLow, \
                btnPoly_2, btnPoly_3, btnPoly_4, btnPoly_5, \
                btnPoly_6, btnPoly_7, btnPoly_8, btnPoly_9, \
                btnApplyChanges, menuOutline]
    
    polys = [btnPoly_2, btnPoly_3, btnPoly_4, btnPoly_5, \
            btnPoly_6, btnPoly_7, btnPoly_8, btnPoly_9]
    
    
    # Set up hamburger menu + activate buttons
    for item in subMenu:
        if type(item) == Text or type(item) == Rectangle or type(item) == Image or type(item) == IntEntry:
            item.undraw()
        else:
            item.activate()
            item.undraw()

    
    # ---------------------------- WIN QR ABOUT ------------------------------

    winQR = DEGraphWin(title = "QR", width = 575, height = 225,
                      offsets = [x+225,y+85], autoflush = False,
                      hasTitlebar = False, hThickness=0, hBGColor='white')
    winQR.setBackground(dark)
    myWindows.append(winQR)

    #add image of qr code
    imgQR = Image(Point(-6,0), here+"/img/qrAbout.png")
    imgQR.draw(winQR)

    #add text for about
    abt = "\n\
    While you wait for the default fractal, (z^3) – 1,\n \
    to generate, scan the QR code to learn about  \n \
        Newton's Method and how to use the exporer.\
    "
    txtAbout = Text(Point(2.75,-1.5), abt, 'avenir', 'white', 14)
    txtAbout.draw(winQR)


    # ---------------------------- WIN FRACTAL ------------------------------

    winFract = DEGraphWin(title = "fractal", width = 575, height = 575,
                      offsets = [x+225,y+310], autoflush = False,
                      hasTitlebar = False, hThickness=0, hBGColor='white')
    winFract.setBackground(dark)
    myWindows.append(winFract)

    # init & create fractal
    fractal = Polynomial_Newtons(window=winFract)


    # -------------------------- INTERACTION -----------------------------

    clickPt = winCP.getMouse()
    currBG = 0  #dark mode vs. light mode color (0: dark, 1: light)
    btnOpen = 0   #hide vs. show buttons (0: hide, 1: show)
    fractMenu = 0   #hide vs. show color / fractal menu (0: hide, 1: show)

    # closed hamburger menu
    for btn in buttons:
        btn.undraw()


    def play_jeopardy():
        os.system('python3 ../util/jeopardy_player.py')

    def on_apply_changes():
        # play Jeopardy music in a separate process / thread
        jeopardy_thread = Thread(target=play_jeopardy)
        jeopardy_thread.start()

        # draw fractal
        fractal.drawFract()

        #join music thread here
        jeopardy_thread.join()

    
    while not btnExit.clicked(clickPt):     
        clickPt = winCP.getMouse()  #perform clicks

        # TOGGLE DARK MODE (default: currBG = 0) / LIGHT MODE (currBG = 1)
        if btnBGColor.clicked(clickPt):
            if currBG == 0:
                for win in myWindows:
                    if win != winHead:
                        win.setBackground(light)
                btnMenu.changeButtonColorTo(light)
                btnMenu.setClickedColors(light, '#03b5fc')
                currBG = 1

            elif currBG == 1:
                for win in myWindows:
                    if win != winHead:
                        win.setBackground(dark)
                btnMenu.changeButtonColorTo(dark)
                btnMenu.setClickedColors(dark, '#03b5fc')
                currBG = 0
        
        # OPEN / CLOSE HAMBURGER MENU
        if btnMenu.clicked(clickPt):
            if btnOpen == 1:
                for btn in buttons:
                    btn.draw(winCP)
                btnMenu.changeLabelColorTo('#7362a1')
                btnOpen = 0

            elif btnOpen == 0:
                for btn in buttons:
                    btn.undraw()
                btnMenu.changeLabelColorTo('white')
                btnOpen = 1

        # SHOW ABOUT + INSTRUCTION MANUAL
        if btnAbout.clicked(clickPt):
            webbrowser.open_new("https://docs.google.com/document/d/1dr6YwybvwNYen1aUUZgJC-sEnj-OaDnG8QI-ORwwfhM/edit?usp=sharing")

        # ZOOM-IN
        if btnZmIn.clicked(clickPt):
            zoomCount += 1
            ratio = winFract.zoom(winControl=winFract, whichWay='in')
            winFract.clear()
            fractal.updateRatio(ratio, zoomCount)
            fractal.changeRes(fractal.mag)
            fractal.drawFract()
        
        # ZOOM-OUT
        if btnZmOut.clicked(clickPt):
            zoomCount = 0
            fractal.ratio = 1
            fractal.changeRes(fractal.mag)
            winFract.zoom(winControl=winFract, whichWay='out')
            winFract.clear()
            fractal.drawFract()
        

        # OPEN / CLOSE COLOR MENU
        if btnOpenColorMenu.clicked(clickPt):
            if fractMenu == 0:
                for item in subMenu:
                    if type(item) == Button:
                        item.activate()
                    item.draw(winCP)
                fractMenu = 1
            else:
                for item in subMenu:
                    item.undraw()
                fractMenu = 0

        # APPLY COLOR MENU CHANGES AND REGENERATE FRACTAL
        if btnApplyChanges.clicked(clickPt):
            # CHANGE ITERS
            iters = entryNumIters.getValue()
            fractal.changeIters(iters)
            on_apply_changes()
        
        # CHANGE POLYNOMIAL DEGREE FROM COLOR MENU
        for i in range(8):
            if polys[i].clicked(clickPt):
                deg = i+2
                fractal.changeDegree(deg)
                break

        # CHANGE PALETTE OPTION
        if btnPalOption1.clicked(clickPt):
            fractal.changePal(0)
        if btnPalOption2.clicked(clickPt):
            fractal.changePal(1)
        if btnPalOption3.clicked(clickPt):
            fractal.changePal(2)

        # SHUFFLE COLORS WITHIN PALETTE
        if btnShuffle.clicked(clickPt):
            fractal.shufflePal()

        # CHANGE RESOLUTION
        if btnMed.clicked(clickPt):
            fractal.changeRes('med')
        elif btnLow.clicked(clickPt):
            fractal.changeRes('low')
        elif btnHi.clicked(clickPt):
            fractal.changeRes('high')

        # CLEAR ALL WINDOWS
        if btnClear.clicked(clickPt):
            zoomCount = 0
            fractal.ratio = 1
            fractal.changeRes(fractal.mag)
            winFract.zoom(winControl=winFract, whichWay='out')
            winFract.clear()
            fractal = Polynomial_Newtons(winFract)

    # QUIT & CLOSE PROGRAM + ALL WINDOWS
    for win in myWindows:
        win.close()


if __name__ == '__main__':
    main(0,0)
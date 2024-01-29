# Author: Radha Munver
# Date: 01/29/2024
# (AT) Nonlinear Dynamics
# UI for Super Mandelbrot Set Explorer


# IMPORTS ------------------------

import sys
sys.path.append("../util")

from tkinter import *
from DEgraphics_Radha import *
from mandelbrotSet import *
from juliaSet import *
import webbrowser
from threading import Thread
import os
from tkinter.colorchooser import askcolor


# MAIN ---------------------------

def main(x,y):
    
    global dark, light
    dark = '#464b4f'
    light = '#959ca1'
    cText = '(0.365, -0.37)'
    cVal = complex(0.365,-0.37)
    iters = 250
    twoTone = False

    myWindows = []
    buttons = []

    # -------------------------------- HEADER -----------------------------------

    winHead = DEGraphWin(title = "header", width = 1125, height = 60,
                      defCoords = [-12,-4,12,4],
                      offsets = [x,y], autoflush = False,
                      hasTitlebar = False, hThickness=0, hBGColor='black')
    winHead.setBackground("#363637")
    myWindows.append(winHead)

    #create & style header text
    txtHead = Text(Point(0,0),"Super Mandelbrot Set Explorer", 'times new roman',
                   'white', 14)
    txtHead.setStyle('italic')
    txtHead.draw(winHead)


    # ----------------------------- CONTROL PANEL -------------------------------

    winCP = DEGraphWin(title = "", width = 225, height = 700,
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
    btnAbout = Button(winCP, topLeft = Point(-7,7.25), width=14, height=0.7,
                edgeWidth = 1, label = 'About', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#e2daf5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)
    buttons.append(btnAbout)
    
    # change background color button (dark/light mode)
    btnBGColor = Button(winCP, topLeft = Point(-7,6.25), width=14, height=0.7,
                edgeWidth = 1, label = 'Dark / Light Mode', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#e2daf5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)
    buttons.append(btnBGColor)
    
    # mandelbrot zoom-in btn
    MbtnZmIn = Button(winCP, topLeft = Point(-7,5.25), width=6.5, height=0.7,
                edgeWidth = 1, label = 'M: Zoom-In', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#e2daf5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)
    buttons.append(MbtnZmIn)
    
    # mandelbrot zoom-out btn
    MbtnZmOut = Button(winCP, topLeft = Point(0.5,5.25), width=6.5, height=0.7,
                edgeWidth = 1, label = 'M: Zoom-Out', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#e2daf5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)
    buttons.append(MbtnZmOut)

    # julia zoom-in btn
    JbtnZmIn = Button(winCP, topLeft = Point(-7,4.25), width=6.5, height=0.7,
                edgeWidth = 1, label = 'J: Zoom-In', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#e2daf5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)
    buttons.append(JbtnZmIn)

    # julia zoom-out btn
    JbtnZmOut = Button(winCP, topLeft = Point(0.5,4.25), width=6.5, height=0.7,
                edgeWidth = 1, label = 'J: Zoom-Out', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#e2daf5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)
    buttons.append(JbtnZmOut)

    # mbrot clear
    MbtnClear = Button(winCP, topLeft = Point(-7,3.25), width=6.5, height=0.7,
                edgeWidth = 1, label = 'M: Clear', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#e2daf5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)
    buttons.append(MbtnClear)

    # julia clear
    JbtnClear = Button(winCP, topLeft = Point(0.5,3.25), width=6.5, height=0.7,
                edgeWidth = 1, label = 'J: Clear', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#e2daf5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)
    buttons.append(JbtnClear)
    
    # quit program btn
    btnExit = Button(winCP, topLeft = Point(-7,2.25), width=14, height=0.7,
                edgeWidth = 1, label = 'Quit Program', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#e2daf5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)
    buttons.append(btnExit)

    
    txtColorChoose = Text(Point(0,-0.25), 'Palette Selection', 'times new roman', 'white', 12)
    txtColorChoose.setStyle('italic')
    txtColorChoose.draw(winCP)
    buttons.append(txtColorChoose)

    # dual tone / single tone [button, dropdown]
    btnDualTone = Button(winCP, topLeft = Point(-9,-0.75), width=8.5, height=0.6,
                edgeWidth = 1, label = 'Dual Tone', radius=10,
                buttonBG = '#a3a5a7', txtColor = 'white',
                clickedBG = '#e2daf5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)
    btnDualTone.setEdgeColor(dark)
    buttons.append(btnDualTone)

    chooseOneTone = DropDown(default='Single Tone',topLeft = Point(4.5,-1.07), choices=['1T:Blue','1T:Red', '1T:Green','1T:None'],font=('avenir',11,'italic'),bg=dark)
    buttons.append(chooseOneTone)

    # apply changes
    btnApply = Button(winCP, topLeft = Point(-4.5,-8.25), width=8.5, height=0.7,
                edgeWidth = 1, label = 'Apply Changes', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#e2daf5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)
    
    btnMenu.activate()
    btnAbout.activate()
    btnBGColor.activate()
    MbtnZmIn.activate()
    MbtnZmOut.activate()
    JbtnZmIn.activate()
    JbtnZmOut.activate()
    MbtnClear.activate()
    JbtnClear.activate()
    btnExit.activate()
    btnDualTone.activate()
    btnApply.activate()

    # undraw buttons for closed hamburger menu
    for btn in buttons:
        btn.undraw()

    # author / about
    txtAuthor = Text(Point(3.75,9.05), 'Radha Munver\nJan. 2024', 'avenir', 'white', 9)
    txtAuthor.setStyle('italic')
    txtAuthor.draw(winCP)


    # ALGORITHM ----------------------------

    txtAlgoSelect = Text(Point(0,-3), 'Select Algorithm', 'times new roman', 'white', 12)
    txtAlgoSelect.setStyle('italic')
    algos = DropDown(default='Select Algorithm',topLeft = Point(0,-3.75), choices=['Escape', 'Inverse'],font=('times new roman',15),bg=dark)
    algos.draw(winCP)
    txtAlgoSelect.draw(winCP)


    # ITERS & C-Value ------------------------

    txtMaxIters = Text(Point(5.5,-6.5),'Max Iterations:\t\t\t\t[0,1000]', 'times new roman',
                        'white', 12)

    entryNumIters = IntEntry(center=Point(2.5,-6.5), width=5, span = [0,1000],
                            colors=['gray','black'],
                            errorColors=['red','white'])
    entryNumIters.setDefault(50)
    entryNumIters.setText(iters)
    entryNumIters.draw(winCP)
    txtMaxIters.draw(winCP)


    txtCValue = Text(Point(4.5,-5.5),'C-Value:\t\t\t\t(real, imag)', 'times new roman',
                        'white', 12)


    # C-Val Formatting: '([real], [imag])'
    entryCVal = Entry(center=Point(2.5,-5.5), width=12)
    entryCVal.setText(cText)
    entryCVal.draw(winCP)
    txtCValue.draw(winCP)

    
    # ---------------------------- WIN QR ABOUT ------------------------------

    winQR = DEGraphWin(title = "QR", width = 899, height = 248,
                      offsets = [x+225,y+535], autoflush = False,
                      hasTitlebar = False, hThickness=0, hBGColor='white')
    winQR.setBackground(dark)
    myWindows.append(winQR)

    #add image of qr code
    here = os.path.dirname(os.path.abspath(__file__))
    imgQR = Image(Point(-6,0), here+"/img/qrAbout.png")
    imgQR.draw(winQR)

    #add text for about
    abt = "\n\
    While you wait for the default Mandelbrot Set and respective Julia Set\n \
    to generate, (z^2) + c, where c = 0.365 - 0.37j, scan the QR code to  \n \
        the left to learn about the Mandelbrot Set and how to use the explorer.\
    "
    txtAbout = Text(Point(2.5,-1), abt, 'avenir', 'white', 14)
    txtAbout.draw(winQR)


    # ---------------------------- WIN MANDELBROT ------------------------------

    winMSet = DEGraphWin(title = "mbrot", width = 448, height = 448,
                      offsets = [x+225,y+85], autoflush = False,
                      hasTitlebar = False, hThickness=0, hBGColor='white')
    winMSet.setBackground(dark)
    myWindows.append(winMSet)

    # init & create mandelbrot set
    mandelbrot = MandelbrotSet(448,448)
    mandelbrot.escapePlotSet(maxIters=250)
    mandelbrot.window.update()


    # ---------------------------- WIN JULIA ------------------------------

    winJSet = DEGraphWin(title = "jset", width = 448, height = 448,
                      offsets = [x+675,y+85], autoflush = False,
                      hasTitlebar = False, hThickness=0, hBGColor='white')
    
    julia = JuliaSet(448,448)
    constant = cVal
    julia.escapePlotSet(const=constant)
    julia.win.update()


    # -------------------------- INTERACTION -----------------------------

    clickPt = winCP.getMouse()
    currBG = 0  #dark mode vs. light mode color (0: dark, 1: light)
    btnOpen = 0   #hide vs. show buttons (0: hide, 1: show)

    # closed hamburger menu
    for btn in buttons:
        btn.undraw()

    
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
                btnDualTone.setEdgeColor(light)
                btnDualTone.setButtonColor('light gray')
                chooseOneTone.setBGColor(light)
                algos.setBGColor(light)
                currBG = 1

            elif currBG == 1:
                for win in myWindows:
                    if win != winHead:
                        win.setBackground(dark)
                btnMenu.changeButtonColorTo(dark)
                btnMenu.setClickedColors(dark, '#03b5fc')
                btnDualTone.setEdgeColor(dark)
                btnDualTone.setButtonColor('#a3a5a7')
                chooseOneTone.setBGColor(dark)
                algos.setBGColor(dark)
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
            webbrowser.open_new("https://docs.google.com/document/d/1fM1h9yf0YkTjsR7gsfWB0g1rpjjyUGDi8yZg7PoqiIY/edit?usp=sharing")


        # ZOOM-IN
        if MbtnZmIn.clicked(clickPt):
            winMSet.clear()
            mandelbrot.zoom(inout='in', iterates=iters, tones=twoTone)

        if JbtnZmIn.clicked(clickPt):
            winJSet.clear()
            julia.zoom(inout='in',constant=cVal,algo=algos.getChoice(),iterates=iters)
        
        # ZOOM-OUT
        if MbtnZmOut.clicked(clickPt):
            winMSet.clear()
            mandelbrot.zoom(inout='out',iterates=iters,tones=twoTone)
        
        if JbtnZmOut.clicked(clickPt):
            winJSet.clear()
            julia.zoom(inout='out',iterates=iters, constant=cVal)

        
        # CHANGE COLOR SCHEMES
        if btnDualTone.clicked(clickPt):
            twoTone = True
            color1 = askcolor(color=None, title='Color Picker')[0]
            color2 = askcolor(color=None, title='Color Picker')[0]
            mandelbrot.clear()
            mandelbrot.escapePlotSet(maxIters=iters, start_color=color1, end_color=color2, twoTone=True)


        # CHANGE ALGORITHM
        if btnApply.clicked(clickPt):

            # Update C-Val and Iters
            choice = algos.getChoice()
            print(f"Algorithm Set To: {choice}")
            iters = entryNumIters.getValue()
            cText = entryCVal.getText().strip('()').split(', ')
            cVal = complex(float(cText[0]),float(cText[1]))
            
            # Update Algorithm, Iters, and cVal in J-Set Plot
            julia.clear()
            if choice == 'Escape':
                julia.escapePlotSet(const=cVal, maxIters=iters)
            if choice == 'Inverse':
                julia.inversePlotSet(const=cVal)
            
            # SINGLE TONE APPLY CHANGES [MSET ONLY]
            if chooseOneTone.getChoice() != '1T:None':
                twoTone = False
                mandelbrot.clear()
                mandelbrot.escapePlotSet(maxIters=iters, single=chooseOneTone.getChoice(), twoTone=False)
                
            mandelbrot.window.update()
            julia.win.update()


        # CLEAR ALL WINDOWS
        if MbtnClear.clicked(clickPt):
            mandelbrot.clear()
        
        if JbtnClear.clicked(clickPt):
            julia.clear()


    # QUIT & CLOSE PROGRAM + ALL WINDOWS
    for win in myWindows:
        win.close()


if __name__ == '__main__':
    main(0,0)
import sys
sys.path.append("../util")

# IMPORTS ------------------------
from tkinter import *
from DEgraphics_Radha import *
from bifurcationDiagram import *
from cobWebDiagram import *
from timeSeriesPlot import *
import webbrowser

def main(x,y):
    
    global dark, light
    dark = '#464b4f'
    light = '#959ca1'
    x0 = 0.3
    r = 1.1
    trans = 0
    iters = 30

    myWindows = []
    buttons = []

    # -------------------------------- HEADER -----------------------------------

    winHead = DEGraphWin(title = "header", width = 900, height = 60,
                      defCoords = [-12,-4,12,4],
                      offsets = [x,y], autoflush = False,
                      hasTitlebar = False, hThickness=0, hBGColor='black')
    winHead.setBackground("white")
    myWindows.append(winHead)

    #create & style header text
    txtHead = Text(Point(0,0),'Logistic Map Explorer', 'times new roman',
                   'black', 14)
    txtHead.setStyle('italic')
    txtHead.draw(winHead)


    # ----------------------------- CONTROL PANEL -------------------------------

    winCP = DEGraphWin(title = "controlPanel", width = 200, height = 800,
                      offsets = [x,y+85], autoflush = False,
                      hasTitlebar = False, hThickness=0, hBGColor='white')
    winCP.setBackground(dark)
    myWindows.append(winCP)
    

    # hamburger menu
    btnMenu = Button(winCP, topLeft = Point(-7.8,9.5), width=3, height=0.7,
                edgeWidth = 0, label = '☰', radius=0,
                buttonBG = dark, txtColor = 'white',
                clickedBG = dark, clickedTxtColor = '#2da0ed',
                font=('avenir', 27, 'bold'), timeDelay = 0.2)

    # about
    btnAbout = Button(winCP, topLeft = Point(-7,8), width=14, height=0.7,
                edgeWidth = 1, label = 'About', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#bfe6f5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)
    buttons.append(btnAbout)
    
    # change background color button (dark/light mode)
    btnBGColor = Button(winCP, topLeft = Point(-7,7), width=14, height=0.7,
                edgeWidth = 1, label = 'Dark / Light Mode', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#bfe6f5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)
    buttons.append(btnBGColor)
    
    # bifurcation zoom-in btn
    btnZmIn = Button(winCP, topLeft = Point(-7,6), width=14, height=0.7,
                edgeWidth = 1, label = 'Zoom-In', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#bfe6f5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)
    buttons.append(btnZmIn)
    
    # bifurcation zoom-out btn
    btnZmOut = Button(winCP, topLeft = Point(-7,5), width=14, height=0.7,
                edgeWidth = 1, label = 'Zoom-Out', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#bfe6f5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)
    buttons.append(btnZmOut)
    
    # get R-val from bifurcation btn
    btnFetchR = Button(winCP, topLeft = Point(-7,4), width=14, height=0.7,
                edgeWidth = 1, label = 'Fetch R-Value', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#bfe6f5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)
    buttons.append(btnFetchR)

    # activate user input panel to enter inputs btn
    btnUserInput = Button(winCP, topLeft = Point(-7,3), width=14, height=0.7,
                edgeWidth = 1, label = 'Input Values', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#bfe6f5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)
    buttons.append(btnUserInput)
    
    # clear times series & cobweb wins btn
    btnClear = Button(winCP, topLeft = Point(-7,2), width=14, height=0.7,
                edgeWidth = 1, label = 'Clear', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#bfe6f5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)
    buttons.append(btnClear)
    
    # quit program btn
    btnExit = Button(winCP, topLeft = Point(-7,1), width=14, height=0.7,
                edgeWidth = 1, label = 'Quit Program', radius=10,
                buttonBG = 'white', txtColor = 'black',
                clickedBG = '#bfe6f5', clickedTxtColor = 'black',
                font=('avenir', 11, 'italic'), timeDelay = 0.2)
    buttons.append(btnExit)
    
    btnMenu.activate()
    btnAbout.activate()
    btnZmIn.activate()
    btnZmOut.activate()
    btnFetchR.activate()
    btnClear.activate()
    btnExit.activate()
    btnBGColor.activate()
    btnUserInput.activate()

    # undraw buttons for closed menu
    for btn in buttons:
        btn.undraw()

    instruction = "\n\
    Open the menu above \n and click 'About' to read \n the documentation prior to \n \
    using the Logistic Map \n    Explorer. Thank you! \
    "
    txtInstruction = Text(Point(0.5,-7), instruction, 'times new roman', 'white', 10)
    txtInstruction.draw(winCP)
    txtAuthor = Text(Point(0.5,-9), 'Radha Munver\nOct. 2023', 'avenir', '#0078e0', 11)
    txtAuthor.setStyle('bold')
    txtAuthor.draw(winCP)
    

    # -------------------------- BIFURCATION DIAGRAM ----------------------------

    winBD = DEGraphWin(title = "bifurcationDiagram", width = 700, height = 275,
                      offsets = [x+200,y+85], autoflush = False,
                      hasTitlebar = False, hThickness=0, hBGColor='white')
    winBD.setBackground(dark)
    myWindows.append(winBD)

    # init & create bifurcation diagram
    bifurcationWin = BifurcationDiagram(window=winBD)
    bifurcationWin.flushing = True

    # header for bif
    txtBifHeader = Text(Point(2,0.9),'Bifurcation Diagram', 'avenir', 'white', 12)
    txtBifHeader.draw(winBD)


    # ---------------------------- COBWEB DIAGRAM -------------------------------

    winCobWeb = DEGraphWin(title = "cobWebDiagram", width = 350, height = 275,
                      offsets = [x+200,y+360], autoflush = False,
                      hasTitlebar = False, hThickness=0, hBGColor='white')
    winCobWeb.setBackground(dark)
    myWindows.append(winCobWeb)

    # init and create cobweb diagram using default vals (see line 16)
    cobWebWin = CobwebDiagram(window=winCobWeb)

    # header for cobweb
    txtCobHeader = Text(Point(0.55,1),'Cobweb Diagram', 'avenir', 'white', 12)
    txtCobHeader.draw(winCobWeb)
    

    # -------------------------- TIME SERIES PLOT ----------------------------

    winTimeSeries = DEGraphWin(title = "cobWebDiagram", width = 350, height = 275,
                      offsets = [x+550,y+360], autoflush = False, axisStyle='dotted',
                      hasTitlebar = False, hThickness=0, hBGColor='white')
    winTimeSeries.setBackground(dark)
    myWindows.append(winTimeSeries)

    # init and create time series plot using default vals (see line 16)
    timeSeries = TimeSeriesPlot(window=winTimeSeries)

    # header for time series
    txtTimeSeries = Text(Point(2.55,1.35),'Time Series Plot', 'avenir', 'white', 12)
    txtTimeSeries.draw(winTimeSeries)


    # ------------------------- INFO / INPUT ----------------------------

    winInfoInput = DEGraphWin(title = "Input Values", width = 700, height = 250,
                      offsets = [x+200,y+635], autoflush = False,
                      hasTitlebar = False, hThickness=0, hBGColor='white')
    winInfoInput.setBackground(dark)
    myWindows.append(winInfoInput)

    # btn for deactivating input panel and plotting diagrams using the new inputs
    btnDone = Button(winInfoInput, topLeft = Point(5.3,6), width = 4, height = 2,
                 edgeWidth = 2, label = 'Activate Inputs', radius=10,
                 buttonBG = 'white', txtColor = 'black',
                 clickedBG = '#bfe6f5', clickedTxtColor = 'black',
                 font=('avenir', 11, 'italic'))
    
    btnDone.activate()

    
    #ENTRY BOXES ---------

    entryNumIters = IntEntry(center=Point(-4,3), width=10, span = [0,500],
                                colors = ['white', 'black'],
                                errorColors=['red', 'white'])
    entryNumIters.setDefault(30)
    entryNumIters.setText(iters)
    entryNumIters.draw(winInfoInput)

    entryTransientBif = IntEntry(center=Point(-4,0), width=10, span = [0,500],
                            colors = ['white', 'black'],
                            errorColors=['red', 'white'])
    entryTransientBif.setDefault(10)
    entryTransientBif.setText(trans)
    entryTransientBif.draw(winInfoInput)

    entryInitX = DblEntry(center=Point(-4,-3), width=10, span = [0,1],
                                colors = ['white', 'black'],
                                errorColors=['red', 'white'])
    entryInitX.setText(x0)
    entryInitX.draw(winInfoInput)

    entrySetR = DblEntry(center=Point(-4,-6), width=10, span = [0,4],
                                colors = ['white', 'black'],
                                errorColors=['red', 'white'])
    entrySetR.setText(r)
    entrySetR.draw(winInfoInput)


    #ENTRY TEXT DESCRIPTIONS & VALID RANGES ---------
    
    txtInputHeader = Text(Point(0,7),'User Input Panel', 'avenir',
                         'white', 18)

    txtNumIters = Text(Point(-4.5,3),'Enter # Iterations:\t\t\t\t[0,500]', 'times new roman',
                         'white', 12)
    txtTransIters = Text(Point(-4.5,0),'Enter # Transients\t\t\t\t[0,500]', 'times new roman',
                         'white', 12)
    txtInitX = Text(Point(-4.5,-3),'Enter Initial x:\t\t\t\t[0,1]', 'times new roman',
                         'white', 12)
    txtEnterR = Text(Point(-4.5,-6),'Enter Custom R:\t\t\t\t[0,4]', 'times new roman',
                         'white', 12)
    
    txtInputHeader.draw(winInfoInput)
    txtNumIters.draw(winInfoInput)
    txtTransIters.draw(winInfoInput)
    txtInitX.draw(winInfoInput)
    txtEnterR.draw(winInfoInput)


    #ENTRY TEXT TIPS ----------

    reminder = '\n\
    Reminder that you must click\n\
    "Input Values" prior to editing values,\n\
    then click "Activate Inputs"\n\
    before resuming use of the explorer.\n\
    More info in "About."'
    
    txtReminder = Text(Point(5.25,-2),reminder,'times new roman','grey',14)
    txtReminder.setStyle('italic')
    txtReminder.draw(winInfoInput)

    border = RoundedRectangle(Point(9.25,2), Point(1.5,-7), -10)
    border.draw(winInfoInput)

    # -------------------------- INTERACTION -----------------------------

    clickPt = winCP.getMouse()
    currBG = 0  #dark mode vs. light mode color (0: dark, 1: light)
    btnOpen = 0   #hide vs. show buttons (0: hide, 1: show)
    titleBarStatus = False  #show vs. hide title-bar (False: hidden, True: shown)

    # closed hamburger menu
    for btn in buttons:
        btn.undraw()

    while not btnExit.clicked(clickPt):     #perform clicks
        clickPt = winCP.getMouse()

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
                btnMenu.changeLabelColorTo('#036bfc')
                btnOpen = 0

            elif btnOpen == 0:
                for btn in buttons:
                    btn.undraw()
                btnMenu.changeLabelColorTo('white')
                btnOpen = 1

        # SHOW ABOUT + INSTRUCTION MANUAL
        if btnAbout.clicked(clickPt):
            webbrowser.open_new("https://docs.google.com/document/d/1BK1jnZlocrtS1Aobvg3Qip3Gt2A5pC5JJv0VnzmF8tM/edit?usp=sharing")

        # ZOOM IN / OUT BIFURCATION
        if btnZmIn.clicked(clickPt):
            winBD.zoom(winControl=winCP, whichWay='in')
            winBD.clear()
            bifurcationWin.drawBifurcationDiagram()
        
        if btnZmOut.clicked(clickPt):
            winBD.clear()
            bifurcationWin = BifurcationDiagram(window=winBD)
        
        # FETCH R-VALUE & RE-GRAPH COBWEB + TIME SERIES USING NEW R
        if btnFetchR.clicked(clickPt):
            R = bifurcationWin.fetch_R()
            print(f"R is now: {R}")
            entrySetR.setText(R)
            cobWebWin.setRX(r,entryInitX.getValue())
            cobWebWin.drawCobwebDiagram(numIters=iters, numTrans=trans)
            timeSeries.plotTimeSeries(R, x0, trans, iters)

        # CLEAR ALL WINDOWS
        if btnClear.clicked(clickPt):
            for win in myWindows:
                if win != winCP:
                    win.clear()
            timeSeries.clearTimeSeries()
            bifurcationWin.drawBifurcationDiagram()

        # TOGGLE TITLE BAR FOR USER INPUT
        if btnUserInput.clicked(clickPt):
            if titleBarStatus == False:
                winInfoInput.toggleTitleBar(True)
                titleBarStatus = True
                clickPt = winInfoInput.getMouse()
                print("Processing request, please wait...")

                # allow for changing of input vals
                while not btnDone.clicked(clickPt):
                    clickPt = winInfoInput.getMouse()
                
                # update status of params
                iters  = entryNumIters.getValue()
                trans = entryTransientBif.getValue()
                x0 = entryInitX.getValue()
                r = entrySetR.getValue()
                
                # update r & x0 for cobweb 
                # then plot cobweb & time series according to updated vals
                cobWebWin.setRX(r,x0)
                cobWebWin.drawCobwebDiagram(numIters=iters, numTrans=trans)
                timeSeries.plotTimeSeries(r, x0, trans, iters)
                
                # close title-bar for input panel to signify deactivation
                winInfoInput.toggleTitleBar(False)
                titleBarStatus = False

    # QUIT & CLOSE PROGRAM + ALL WINDOWS
    for win in myWindows:
        win.close()


if __name__ == '__main__':
    main(0,0)
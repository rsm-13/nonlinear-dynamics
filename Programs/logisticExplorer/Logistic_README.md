Radha Munver  |  
October 27, 2023  |  
Nonlinear Dynamics

# Logistic Map Explorer
---

## Introduction

*About the Logistic Map Equation:*
    
- X0 ∈ [0, 1] and R ∈ [0, 4] 
- Xn + 1 = f_R (Xn) = R • Xn • (1 − Xn) 


*Purpose of Explorer:*

Create an interactive interface for which the user can explore the dynamics of the logistic map with ease and make potential discoveries.


*Instructions:*  Click [here]([url](https://github.com/rsm-13/nonlinear-dynamics/blob/main/Programs/logisticExplorer/Logistic_README.md#instructions--tips)) to jump directly to the manual and tips.
(https://github.com/rsm-13/nonlinear-dynamics/blob/main/Programs/logisticExplorer/Logistic_README.md#instructions--tips)

---

## Elements
                    
**Bifurcation diagram**
	- Serves as a roadmap for the dynamics, and primarily serves an interactive guide to examine various R-values.
                        
**Cobweb diagram**
	- Graph shows the iteration for a given number of iterations whose horizontal axis is Xn and whose vertical axis is Xn+1. Displays the graph of f_R (Xn) and the steady-state line (y = x).
                        
**Time-series plot**
	- Plot shows the iterations with Xn as the vertical axis and t as the horizontal axis.
                        
**Control (side) panel**
	- Home for the majority of buttons and functions nested under the hamburger menu.

**User input entry panel**
	- Location where users can customize input parameters (more on how to do this below).

---
        
## Functions & Parameters                                      

The following are the inputs to the program that can be set/changed or used to interact with the explorer:
                    
**iterations to display:** affects both the cobweb diagram and the time-series plot, but not the bifurcation diagram; can choose whole number values in the range [0, 500].
                        
**transient iterations:** affects the same plots as the item above; essentially the number of iterations that you do NOT want to be displayed; range of valid inputs is: [0, 500].
                        
**R-value:** is derived from either the bifurcation diagram (fetch-R) or an entry box. R can be within the range of [0, 4]. You may find the following through exploration:
	- R ∈ [0,1] is stable and attracting
	- R ∈ [1,3] bifurcates into (r – 1) / r as stable attracting…
	- …which bifurcates into 1+√6
	- R ∈1+6, 4]: there exists a range where all periods (of natural numbers) exists

**zooming:** can zoom in and out of the bifurcation diagram
                        
**clearing:** of time series and cobweb diagram

---

## Instructions & Tips

**Instructions & Manual:**

	1. Click the “☰” symbol in the side-panel to open up the menu.
	2. Clicking the symbol once again will collapse the menu.
	3. “About” will bring you to this page for documentation.
	4. Users can choose to toggle the brightness of the interface using light mode (dark mode is default) using the “Dark / Light Mode” button.
	5. Use “Zoom-In” to zoom into the bifurcation diagram;
		1. After clicking “Zoom-In,” click two points on the bifurcation diagram window to draw the rectangular region for which the window will zoom; the two points symbolize the two corners of the rectangle.
		2. Once a black rectangle appears in the window, press “Zoom-In” once again in the side-panel.
	6. “Zoom-Out” will reset the zoom to the default zoom of the bifurcation diagram.
	7. The “Fetch R-Value” button allows the user to click a point on the bifurcation diagram, and use that R-value to re-graph the cobweb diagram and time-series plot. This change will be updated in the user-input panel for the user to see the selected R-value as well.
	8. To input custom values, there are 3 steps:
		1. First click “Input Values” in the side panel.
		2. Once a title bar pops up on the user input window panel, you may manipulate / change the values for # iterations, # transients, R, and x.
		3. Once you are done choosing values, click “Activate Inputs” in the top-right corner, and the updated diagrams should be displayed.
		4. (*See tips for more details or if difficulty arises.)
	9. To clear the bifurcation diagram (and reset it), cobweb diagram, and time series plot, press “Clear.”
	10. “Quit program” will close the application and explorer.
	11. For further questions not answered in this instructions or in the tips below, please email rmunver25@d-e.org. 

**Tips & Reminders:**

	- Please note that in order for the program to successfully accept user input, the “Input Values” button in the side menu must be clicked first, followed by manipulating entries, and then pressing “Activate Inputs” in the input panel to activate the new values. Please do not click any other buttons in between these processes for optimum functionality!
	
	- When inputting values into the user-input panel, it is highly recommended to use the “tab” key to navigate the entry boxes; however, the cursor should also work.
	
	- The program can be slow at times! If this is the case and certain buttons are not appearing clicked, please wait a few seconds then proceed.

---

### Enjoy!

Radha Munver
December 6, 2023
Nonlinear Dynamics

# Newton’s Method Fractal Explorer
---

## Introduction

*About Newton’s Method Formula:*

- *~Definition:~* an iterative scheme for finding the roots of differentiable functions
- Uses a tangent line approximation (linearization) to update an initial guess, until the scheme approaches a root
- It is often difficult, if not impossible, to determine which of the roots an orbit might tend towards, for functions with multiple roots

For a differentiable function, *f*(*z*), an initial guess, z0, is chosen.

*Newton’s Method Equation:*
z_(n+1) = z_n − (f(z_n) / f ′(z_n))

Given a complex-valued function f(z) that has roots z1*, z2*, … , z_k* and a corresponding color map c1, c2, … , c_k, for each point z0 in the complex plane:
	- Newton’s method equation is iterated a specified number of times
	- It is determined which root z_i* is closest
	- The corresponding *c**I*is chosen as the color to plot at the point, *z*0, in the plane
	- If | f(z) | becomes too large, then: z0 = z0 − f(z0) / f'(z0)


*Purpose of Explorer:*

This explorer aims to explore the relationship between initial guesses and the roots that they approach


*Instructions:*	Click [here](https://docs.google.com/document/d/1dr6YwybvwNYen1aUUZgJC-sEnj-OaDnG8QI-ORwwfhM/edit#bookmark=kix.xveryqnvsrw8) to jump directly to the manual and tips.

---

## Elements
				
**About Window**
	1. While the default fractal is being generated, the user may scan the QR code displayed in the ‘About’ window to read these instructions regarding how to operate the Newton’s Method explorer. This document is also accessible in the control panel as a button, but the user will have to wait for the initial fractal’s generation to access the concealed side panel.
	 					
**Fractal Window**
	1. Graph shows the iteration for a given number of iterations whose horizontal axis is *x**t* and whose vertical axis is *x**t*+ 1. Displays the graph of *f**R*(*x**t*) and the steady-state line (*y = x*).
	 					
**Control (side) panel**
	1. Home for the majority of buttons and functions nested under the hamburger menu.

**Color, Resolution, and Polynomial Menu (A.K.A. ‘Fractal Menu’)**
	1. Location where users can customize input parameters (more on how to do this below).
	2. Parameters which can be altered include the degree of the polynomial, the color palette, the order of the colors in the palette (for root correspondence), the resolution of the fractal, and the number of iterations displayed.

---

## Functions & Parameters
					 					
The following are the inputs to the program that can be set/changed or used to interact with the explorer:
					
**iterations to display:** can choose whole number values in the range [0, 100].
		
**degree of polynomial:** can choose a polynomial equation for the fractal with varying ° using the buttons in the Fractal Menu (accessible under hamburger menu). Valid ° include **[2, 9]**. The equation will be in the format of f(z) = (z^n) – 1, where *n* is the degree.
			
**resolution:** the user may select their desired resolution through the fractal menu as well by selecting from the parameters of ‘High,’ ‘Medium,’ and ‘Low.’ In the most zoomed-out state, high, medium, and low will correspond to 0.03, 0.04, and 0.06 PPI, respectively.

**color palette:** the user may select a color palette from the options displayed in the fractal menu for which they would like seen used for the roots on their fractal. The default fractal displayed will choose a random color palette (perhaps using one not displayed in the options in the menu). The user also has the option to ‘shuffle’ the order of the colors in the palette using the ‘reload’ icon button in the fractal menu.

**zooming:** can zoom in and out of the displayed fractal. The resolution adjusts accordingly
	
**clearing:** of fractal window

---

## Instructions & Tips

**Instructions & Manual:**

	1. Click the “☰” symbol in the side-panel to open up the menu.
		1. Clicking the symbol once again will collapse the menu.
	2. “About” will bring you to this page for documentation. (as will the QR code)
	3. Users can choose to toggle the brightness of the interface using light mode (dark mode is default) using the “Dark / Light Mode” button.
	4. Use “Zoom-In” to zoom into the fractal;
		1. After clicking “Zoom-In,” click two points on the fractal window to draw the rectangular region for which the window will zoom; the two points symbolize the two corners of the rectangle.
		2. Once a black rectangle appears in the window, press “Zoom-In” once again in the side-panel.
	5. “Zoom-Out” will reset the zoom to the default zoom of the bifurcation diagram.
	6. The “Color, Res, & Poly Menu” button opens up the fractal menu and allows for parameter changes. See step 7.
	7. To change the parameters and attributes of the fractal:
		1. First click “Color, Res, & Poly Menu” in the side panel.
		2. Once the fractal menu pops up on the user input window panel, you may manipulate / change the # iterations (integer input), the palette, the resolution, and degree of polynomial. You may click a different attribute to change your selection if you are unsatisfied / changed your mind regarding your initial choice.
		3. Once you are done choosing values, click “- [x] ” in the top-left hand corner, and the updated fractal should be displayed using your selected palette, resolution, degree, and number of iterations.
		4. (**See tips for more details or if difficulty arises.)
	8. To clear the fractal diagram, press “Clear.”
	9. “Quit program” will close the application and explorer.
	10. For further questions not answered in this instructions or in the tips below, please email  [rmunver25@d-e.org](mailto:rmunver25@d-e.org) . 


**Tips & Reminders:**

	1. Please note that in order for the program to successfully accept and activate user input, the “- [x] ” button in the fractal menu must be clicked following the manipulation of entries. 

	2. It can take time for higher degree polynomials to generate! Please be patient, and for optimum functionality, ensure that you have minimal other applications open / running and minimal tabs on your browser window. This will ensure efficiency.

	3. Iff you have clicked the ‘- [x] ’ button and you see the loading / colored-spiral icon as a replacement for your mouse, this means the values for the fractal are being calculated and that the fractal should be displayed in its window shortly. The jeopardy music in the background is also a key indicator that the program is working! If the aforementioned features are not true, please try to reset the program using ^C and restart, or contact the author of this program at the email listed in step 10 of the instructions.

	4. Lastly, if you are unable to click in the control panel, try clicking another window for another application, say VS Code or Google, and then return back. It may still be registering the previous request. 

---

### Enjoy!
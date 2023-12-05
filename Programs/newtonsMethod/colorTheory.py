# Author: Radha Munver
# Date: 12/06/2023
# (AT) Nonlinear Dynamics
# Color and Palette Class for Newton's Method Explorer


# IMPORTS ----------------------

import sys
sys.path.append("../util")

import cmath as cm
import numpy as np
from DEgraphics_Radha import *
from random import shuffle
from newtonsFractal import *
import random


# COLOR THEORY CLASS -----------

class ColorTheory:

    # init with first palette
    def __init__(self):
        self.changePal(0)


    # gets color(s) corresponding to the proximity of each point to the roots
    def getColor(self, z_values, roots):
        """
        Get the color for a given set of points based on their proximity to the roots.

        Parameters:
        - z_values (array-like): array of complex numbers representing points in the complex plane
        - roots (array-like): array of complex numbers representing the roots of the polynomial

        Returns:
        - color (str or array): Color(s) corresponding to the proximity of each point to the roots
        """
        # calculate distances b/w each point and the roots
        distances = np.abs(np.subtract.outer(roots, z_values))

        # find index of root with the min dist. for each point
        min_dist_indices = np.argmin(distances, axis=0)

        # if only one point, return color corresponding to its nearest root
        if np.isscalar(min_dist_indices):
            return self.PAL_newtons[min_dist_indices]

        # if multiple pts, return array of colors corresponding to their nearest roots
        if len(min_dist_indices) > 0:
            return np.array([self.PAL_newtons[i] for i in min_dist_indices])

        # handle the case where min_dist_indices is an empty array or list
        return None
    

    # change palette by selecting nth palette in list, 'palettes'
    def changePal(self, nthPal):
    
        #pre1 = ['#D8E0BB','#B6CEC7','#86A3C3','#7268A6','#6B3074']
        #pre2 = ['#355070','#6D597A','#B56576','#E56B7F','#EAAC8B']

        palettes = [ \
        ['#a1b45b', '#7aa599', '#4c719a', '#4e4677', '#461f4b', '#D8E0BB', '#B6CEC7', '#86A3C3', '#7268A6', '#6B3074'], \
        ['#393D3F', '#FDFDFF', '#C6C5B9', '#62929E', '#546A7B', '#376669', '#284B63', '#6F7678', '#555B6E'], \
        ['#FFD6BA', '#DDD1ED', '#3E5C76', '#FAE1DF', '#1D2D44', '#213540', '#B1C9CC', '#89B0AE', '#748CAB', '#F0EBD8'], \
        ['#36413E', '#5D5E60', '#8D8D92', '#BEB2C8', '#D7D6D6'], \
        ['#555B6E', '#89B0AE', '#BEE3DB', '#FAF9F9', '#FFD6BA'], \
        ['#D1CCDC', '#424C55', '#F5EDF0', '#886F68', '#3D2C2E'], \
        ['#424874', '#DCD6F7', '#A6B1E1', '#CACFD6', '#D6E5E3'], \
        ['#000000', '#66666E', '#9999A1', '#E6E6E9', '#F4F4F6'], \
        ['#30292F', '#413F54', '#5F5AA2', '#355691', '#3F4045'], \
        ['#0D1321', '#1D2D44', '#3E5C76', '#748CAB', '#F0EBD8'], \
        ['#0D1F2D', '#546A7B', '#9EA3B0', '#FAE1DF', '#E4C3AD']]

        self.PAL = palettes[nthPal]
        self.PAL_newtons = self.PAL
    

    # shuffle colors within palette
    def shufflePal(self):
        tempPal = self.PAL
        shuffle(tempPal)
        self.PAL = tempPal

    # gets a random palette from 'palette'
    def getRandomPal(self):
        # !note that if a number other than 0, 1, or 2 is selected,
        # only polynomials up to degree 5 can be shown without throwing an index out of bounds error.
        # the user must change the palette in the fractal menu to get a polynomial for degrees ≥ 6
        nthPal = random.randint(0, 9)
        self.changePal(nthPal)
        return self.PAL

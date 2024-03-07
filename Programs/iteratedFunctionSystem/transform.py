# class for an IFS transform, which consists of
# 8 parameters:
#    SCALING/REFLECTION: r and s (horizontal and vertical respectively)
#    ROTATION: theta and phi (horizontal and vertical rotation, respectively)
#    TRANSLATION: h and k (horizontal and vertical shift, respectively)
#    PROBABILITY: p
#    COLOR: c
#
# For a transformation to be "interesting", it needs to be a contraction, which
# means r and s must be no greater than 1 in magnitude. In other words,
#      |r| <= 1 and |s| <= 1
#
# theta and phi will be stored in DEGREES, along with their radian equivalents for
# use in computing actual transformations of points in the plane
#
# no restrictions on h and k
#
# p is always a non-negative WHOLE number, representing a probability weighting
# for that transformation. p = 0 is a way of turning that transformation OFF. The higher
# p is, the more likely it is that the transformation will be selected.
#
# c can be any valid color in python

from math import *

class IFS_Transform:

    def __init__(self, xScale = 0.5, yScale = 0.5,
                 theta = 0.0, phi = 0.0,
                 h = 0.0, k = 0.0,
                 p = 1, c = 'white'):
        # scaling and reflection
        self.r = xScale
        self.s = yScale

        # rotation (rigid if theta = phi)
        self.theta = theta
        self.phi = phi
        self.thetaRadians = radians(self.theta)
        self.phiRadians = radians(self.phi)

        # translation
        self.e = h
        self.f = k

        # probability and color
        self.prob = p
        self.color = c

    def setR(self, xScale):
        '''sets this transform's horizontal scaling/reflection'''
        self.r = xScale

    def setS(self, yScale):
        '''sets this transform's vertical scaling/reflection'''
        self.s = yScale

    def setTheta(self, angle):
        '''sets this transform's rotation for horizontal lines and updates radian equivalent'''
        self.theta = angle
        self.thetaRadians = radians(self.theta)

    def setPhi(self, angle):
        '''sets this transform's rotation for vertical lines and updates radian equivalent'''
        self.phi = angle
        self.thetaPhi = radians(self.phi)

    def setHshift(self, shift):
        '''sets this transform's horizontal shift'''
        self.h = shift

    def setVshift(self, shift):
        '''sets this transform's vertical shift'''
        self.k = shift

    def setProb(self, prob):
        '''sets this transform's probability weighting factor'''
        self.p = prob

    def setColor(self, myColor):
        '''sets this transform's color'''
        self.c = myColor

    # Note on scaling/reflection:
    #   for a contraction-mapping we need r and s to both be no
    #   greater than 1 in magnitude. If r is negative, this implements
    #   a reflection across the y-axis, and if s is negative this implements
    #   a reflection across the x-axis.
    def getR(self):
        '''returns this transform's horizontal scaling/reflection parameter'''
        return self.r

    def getS(self):
        '''returns this transform's vertical scaling/reflection parameter'''
        return self.s

    def getTheta(self):
        '''returns this transform's rotation for horizontal lines'''
        return self.theta

    def getPhi(self):
        '''returns this transform's rotation for vertical lines'''
        return self.phi

    def getE(self):
        '''returns this transform's horizontal shift'''
        return self.e

    def getF(self):
        '''returns this transform's vertical shift'''
        return self.f

    def getProb(self):
        '''returns this transform's probability weighting factor'''
        return self.prob

    def getColor(self):
        '''returns this transform's color'''
        return self.color

    # run the transform once on the point given by (x,y)-tuple pt
    def transformPoint(self, pt):
        newX = pt[0] * self.r * cos(self.thetaRadians) - pt[1] * self.s * sin(self.phiRadians) + self.e
        newY = pt[0] * self.r * sin(self.thetaRadians) + pt[1] * self.s * cos(self.phiRadians) + self.f
        return newX, newY

    def __str__(self):
        #toString method
        result = '[scale(' + str(self.r) + ',' + str(self.s) + '), '
        result += 'rot(' + str(self.theta) + ',' + str(self.phi) + '), '
        result += 'trans(' + str(self.e) + ',' + str(self.f) + '), '
        result += 'prob(' + str(self.prob) + '), '
        result += 'col(' + str(self.color) + ')]'
        return result

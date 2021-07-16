import math


def applyVectorToPosition(position, vector):
    return [position[0] + vector[0], position[1] + vector[1]]

def getRotationalVector(angle):
    '''0 degrees is up'''
    return [math.cos(angle), math.sin(angle)]

def setMagnitude(vector, magnitude):
    return [vector[0] * magnitude, vector[1] * magnitude]

def getMagnitude(vector):
    return math.sqrt(vector[0]**2 + vector[1]**2)
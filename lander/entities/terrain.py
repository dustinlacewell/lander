import random

from lander.consts import *
from lander.geom import *


def randomNumbersInRange(min, max, n):
    return [random.randint(min, max) for i in range(n)]

def generateRandomWalkSequence(n, maxVariance, minValue, maxValue):
    '''
    Generate a list of random values, each varying from the previous by a random amount.
    '''
    # Initialize the sequence with the first value
    sequence = [random.randint(minValue, maxValue)]
    # Generate the rest of the values
    for i in range(1, n + 1):
        # Generate a random value between 0 and maxVariance
        variance = random.randint(0, maxVariance)
        # get random sign
        sign = random.choice([-1, 1])
        # apply variance to previous value
        sequence.append(max(minValue, min(maxValue, sign * variance + sequence[i-1])))
    return sequence

def createLinesFromArrayOfHeights(arrayOfHeights):
    '''
    Draws lines across the screen using a list of heights.
    '''
    lines = []
    # determine width of each segment
    segmentWidth = SCREEN_WIDTH / (len(arrayOfHeights) - 1)
    # save the last value of the array to be used for the next segment
    lastValue = (0, arrayOfHeights[0])
    # draw the rest of the segments
    for i in range(1, len(arrayOfHeights)):
        x = i * segmentWidth
        y = arrayOfHeights[i]
        newValue = (x, y)
        lines.append((lastValue, newValue))
        lastValue = newValue
    return lines

class Terrain:

    def __init__(self, segments, maxChange, minValue):
        self.segments = segments
        self.maxChange = maxChange
        self.minValue = minValue

        points = generateRandomWalkSequence(segments, maxChange, SCREEN_HEIGHT - minValue, SCREEN_HEIGHT)
        self.lines = createLinesFromArrayOfHeights(points)


    def intersectsLine(self, line):
        for lineSegment in self.lines:
            if testLinesIntersect(lineSegment, line):
                return True
        return False

    def intersectsLines(self, lines):
        for line in lines:
            if self.intersectsLine(line):
                return True
        return False

    def intersectsRect(self, rect):
        for line in self.lines:
            if testLineRectIntersect(line, rect):
                return True
        return False

    def intersectsRects(self, rects):
        for rect in rects:
            if self.intersectsRect(rect):
                return True
        return False

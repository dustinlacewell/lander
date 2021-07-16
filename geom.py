from shapely.geometry import LineString, Point


def generatePointsFromArray(array):
    '''
    Given an array of ints, generate a list of points.
    '''
    points = []
    for i in range(len(array) - 1):
        points.append((array[i], array[i+1]))
    return points

def generateLinesFromPoints(points):
    '''
    Given a list of points, generate a list of lines
    '''
    lines = []
    for i in range(len(points) - 1):
        lines.append((points[i], points[i+1]))
    return lines

def getLinesFromRect(rect):
    '''
    returns a list of lines representing the sides of the rect
    '''
    lines = []
    lines.append((rect.topleft, rect.topright))
    lines.append((rect.topright, rect.bottomright))
    lines.append((rect.bottomright, rect.bottomleft))
    lines.append((rect.bottomleft, rect.topleft))
    return lines

def testLinesIntersect(line1, line2):
    l1 = LineString(line1)
    l2 = LineString(line2)
    return l1.intersects(l2)

def testLineRectIntersect(line, rect):
    '''
    Tests if a line intersects a rectangle.
    '''
    lines = getLinesFromRect(rect)
    return any(testLinesIntersect(l, line) for l in lines)

def testLinesRectIntersect(lines, rect):
    '''
    Tests if a line intersects a rectangle.
    '''
    return any(testLineRectIntersect(l, rect) for l in lines)

def testRectRectIntersect(rect1, rect2):
    '''
    Tests if two rectangles intersect.
    '''
    lines = getLinesFromRect(rect1)
    return testLinesRectIntersect(lines, rect2)
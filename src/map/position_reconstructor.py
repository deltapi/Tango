import numpy

from src.map.position import Position


def reconstructPosition(initialBearing, currentBearing, lastPosition, forwardSpeed):
    direction = numpy.radians((initialBearing - currentBearing) % 360)
    newPosition = Position(lastPosition.x + numpy.cos(direction) * forwardSpeed, lastPosition.y + numpy.sin(direction) * forwardSpeed)
    return newPosition

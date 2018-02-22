import numpy

from src.drive.sensor_data import Sensor_data
from src.map.factor_graph_data import FactorGraphData


def reconstructOdometry(receivedSensorData, forwardSpeed):
    if (len(receivedSensorData) == 1):
        dict = {"hmc5883l": {
            "bearing": 0.0
        },
            "infrared": {
                "frontleft": 100.0,
                "frontright": 100.0,
                "rearleft": 100.0,
                "rearright": 100.0
            },
            "ultrasonic": {
                "front": 40.0,
                "rear": 40.0
            },
            "timestamp": 0.0
        }
        sensor_data = Sensor_data(dict)
        return FactorGraphData(0, sensor_data)
    lastSnapshot = receivedSensorData[-2]
    currentSnapshot = receivedSensorData[-1]
    deltaTime = currentSnapshot.timestamp - lastSnapshot.timestamp

    print(currentSnapshot.bearing, lastSnapshot.bearing)

    newSensorData = currentSnapshot
    newSensorData.bearing = 0
    averageTurnAngle = 18
    if forwardSpeed > 0:
        deltaX = deltaTime * forwardSpeed
        odometry = FactorGraphData(deltaX, newSensorData)
    if forwardSpeed == -1:
        deltaX = 0
        deltaBearingInRadians = numpy.pi / 180. * averageTurnAngle
        newSensorData.bearing = deltaBearingInRadians
        odometry = FactorGraphData(deltaX, newSensorData)
    if forwardSpeed == -2:
        deltaX = 0
        deltaBearingInRadians = -numpy.pi / 180. * averageTurnAngle
        newSensorData.bearing = deltaBearingInRadians
        odometry = FactorGraphData(deltaX, newSensorData)

    return odometry

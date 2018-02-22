import numpy


class FactorGraphData():
    def __init__(self, x, deltaBearing, sensorData):
        print(sensorData)
        self.deltaX = x
        self.deltaBearing = deltaBearing  # in radians, and mathematical orientation
        self.currentBearing = sensorData.bearing
        self.observations = self.extractObservations(sensorData)

    def __str__(self):
        return "(" + str(self.deltaX) + "," + str(self.deltaBearing) + ")"

    def extractObservations(self, sensorData):
        irThreshold = 20
        usThreshold = 20
        observations = []

        if sensorData.irFrontLeft < irThreshold:
            observations.append((self.extractOrdinateFromDistance(sensorData.irFrontLeft),
                                 self.extractOrdinateFromDistance(sensorData.irFrontLeft)))

        if sensorData.irFrontRight < irThreshold:
            observations.append((self.extractOrdinateFromDistance(sensorData.irFrontRight),
                                 -self.extractOrdinateFromDistance(sensorData.irFrontRight)))

        if sensorData.irRearLeft < irThreshold:
            observations.append((-self.extractOrdinateFromDistance(sensorData.irRearLeft),
                                 self.extractOrdinateFromDistance(sensorData.irRearLeft)))

        if sensorData.irRearRight < irThreshold:
            observations.append((-self.extractOrdinateFromDistance(sensorData.irRearRight),
                                 -self.extractOrdinateFromDistance(sensorData.irRearRight)))

        if sensorData.usFront < usThreshold:
            observations.append((0, sensorData.usFront))

        if sensorData.usRear < usThreshold:
            observations.append((0, -sensorData.usRear))

        return observations

    def extractOrdinateFromDistance(self, distance):
        return numpy.sqrt(distance ** 2 / 2)

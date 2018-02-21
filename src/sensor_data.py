import numpy


class Sensor_data():

    def __init__(self, dict):
        self.irFrontLeft = dict['infrared']['frontleft']
        self.irFrontRight = dict['infrared']['frontright']
        self.irRearLeft = dict['infrared']['rearleft']
        self.irRearRight = dict['infrared']['rearright']
        self.usFront = dict['ultrasonic']['front']
        self.usRear = dict['ultrasonic']['rear']

    def getDetectedDistances(self):
        return numpy.array([
            [0, self.usFront],
            [numpy.pi / 4, self.irFrontLeft],
            [3 * numpy.pi / 4, self.irRearLeft],
            [numpy.pi, self.usRear],
            [-3 * numpy.pi / 4, self.irRearRight],
            [-numpy.pi / 4, self.irFrontRight],
        ])

    def getNearestDetectedAngleAndDistance(self):
        index = numpy.argmin(self.getDetectedDistances()[:, 1])
        return self.getDetectedDistances()[index, :]

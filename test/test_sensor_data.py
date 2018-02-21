from src.drive.sensor_data import Sensor_data


def test_sensor_data_getDetectedDistances():
    sensorValues = {'hmc5883l': {'bearing': 32.58082580566406},
                    'timestamp': 1519221800.0643256,
                    'ultrasonic': {'front': 29.0, 'rear': 40.0},
                    'infrared': {'frontleft': 100.0, 'rearleft': 100.0, 'frontright': 18.50337791442871, 'rearright': 32.40828323364258},
                    'cores': {'core1': 9.0, 'core2': 100.0, 'core0': 10.100000381469727, 'core3': 12.600000381469727},
                    'gy521': {'accel': {'x': -6, 'z': 70, 'y': -8},
                              'angle': {'x': -4.936834812164307, 'z': 8.130102157592773, 'y': -6.49618673324585},
                              'gyro': {'x': -3, 'z': -1, 'y': 0}}}

    sensor_data = Sensor_data(sensorValues)

    distances = sensor_data.getDetectedDistances()
    minimalDistance = sensor_data.getNearestDetectedAngleAndDistance()
    print(distances)
    print(minimalDistance)


test_sensor_data_getDetectedDistances()

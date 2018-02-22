from time import sleep


def stop_if_obstacle_within_threshold(roverController, minDistance):
    Threshold = 10
    if (minDistance < Threshold):
        roverController.stop()
        return 0
    else:
        roverController.forward(speed=100)
        return 100


def stop_and_rotate_on_obstacle(roverController, sensorData):
    usThreshold = 30
    irThreshold = 15
    if sensorData.usFront < usThreshold or sensorData.irFrontRight < irThreshold or sensorData.irFrontLeft < irThreshold:
        if sensorData.irFrontLeft > sensorData.irFrontRight:
            roverController.turn_left(400)
        else:
            roverController.turn_right(400)
        sleep(0.2)
        roverController.stop()
        return 0
    else:
        roverController.forward(400)
        return 150

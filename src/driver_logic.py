from time import sleep


def stop_if_obstacle_within_threshold(roverController, minDistance):
    Threshold = 10
    if (minDistance < Threshold):
        roverController.stop()
    else:
        roverController.forward(speed=100)


def stop_and_rotate_on_obstacle(roverController, sensorData):
    usThreshold = 25
    irThreshold = 15
    if sensorData.usFront < usThreshold or sensorData.irFrontRight < irThreshold or sensorData.irFrontLeft < irThreshold:
        if sensorData.irFrontLeft > sensorData.irFrontRight:
            roverController.turn_left(350)
        else:
            roverController.turn_right(350)
        sleep(0.1)
        roverController.stop()
    else:
        roverController.forward(150)

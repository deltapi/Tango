from time import sleep


def stop_if_obstacle_within_threshold(roverController, minDistance):
    Threshold = 10
    print("Min Distance: " + str(minDistance))
    if (minDistance < Threshold):
        roverController.stop()
    else:
        roverController.forward(speed=100)


def stop_and_rotate_on_obstacle(roverController, minFrontDistance):
    Threshold = 35
    print("Min Distance: " + str(minFrontDistance))
    if (minFrontDistance < Threshold):
        roverController.turn_left(150)
        sleep(0.5)
        roverController.stop()
    else:
        roverController.forward(150)

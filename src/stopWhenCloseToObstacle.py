def stopIfObstacleWithinThreshold(roverController, minDistance):
    Threshold = 10
    print("Min Distance: " + str(minDistance))
    if (minDistance < Threshold):
        roverController.stop()
    else:
        roverController.forward(speed=100)

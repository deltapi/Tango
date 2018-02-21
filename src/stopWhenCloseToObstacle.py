def stopIfObstacleWithinThreshold(roverController, minDistance):
    Threshold = 30
    print("Min Distance: " + str(minDistance))
    if (minDistance < Threshold):
        roverController.stop()
    else:
        roverController.forward(speed=100)

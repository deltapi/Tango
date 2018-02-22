landmarkId = 10000


def writeToG2oFile(factorGraphDataList):
    fileContent = createFactorGraphString(factorGraphDataList)
    writeStringToFile(fileContent)


def createFactorGraphString(factorGraphDataList):
    fileContent = ""
    for i in range(len(factorGraphDataList) + 1):
        fileContent += writePose(i, getCurrentBearing(factorGraphDataList, i))
    for i in range(len(factorGraphDataList)):
        fileContent += writeOdometryAndObservations(i, i + 1, factorGraphDataList[i])
    return fileContent


def getCurrentBearing(factorGraphDataList, i):
    if len(factorGraphDataList) < 1 or i >= len(factorGraphDataList):
        return 0
    return factorGraphDataList[i].currentBearing


def writePose(id, currentBearing):
    string = "VERTEX_SE2 {} 0 0 0\n".format(id)
    string += "POSITION_2D_PRIO_FACTOR {} 0 0 {} 1 1 1000\n".format(id, currentBearing)
    return string


def writeOdometryAndObservations(idPreviousPose, idCurrentPose, factorGraphData):
    global landmarkId
    string = "EDGE_SE2 {} {} {} 0 {} 500 0 0 500 0 1\n".format(idPreviousPose, idCurrentPose, factorGraphData.deltaX,
                                                               factorGraphData.deltaBearing)
    for observation in factorGraphData.observations:
        string += "VERTEX_XY {} 0 0\n".format(landmarkId)
        string += "EDGE_SE2_XY {} {} {} {} 1000 0 1000\n".format(idCurrentPose, landmarkId, observation[0], observation[1])
        landmarkId += 1
    return string


def writeStringToFile(fileContent):
    file = open("/tmp/output.txt", "w")
    file.write(fileContent)
    file.close()

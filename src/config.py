ROVER_ID = 1
TOPIC = "rover/{}/RoverDriving/control".format(ROVER_ID)
HOSTNAME = "bcx-hono.eastus.cloudapp.azure.com"
PORT = 1883
AUTH = {'username': "rover{}@DEFAULT_TENANT".format(ROVER_ID),
        'password': "hono-rover{}".format(ROVER_ID)}

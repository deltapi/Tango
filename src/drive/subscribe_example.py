#!/usr/bin/env python3
import json
import time

import paho.mqtt.client as mqtt

import src.config as cfg
import src.drive.driver_logic as driver_logic
from src.drive.rover_commands import Rover
from src.drive.sensor_data import Sensor_data
from src.map.g2o_translator import writeToG2oFile
from src.map.factor_graph_data_reconstructor import reconstructOdometry
from src.map.position import Position
from src.map.position_reconstructor import reconstructPosition

telemetry = []
logfile = open("/tmp/rover_sensor.log", "a")
positions = []
receivedSensordata = []
receivedOdometryData = []
initialBearing = -1.0


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(cfg.topic_telemetry, qos=0)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global initialBearing
    frame = json.loads(msg.payload.decode('utf8'))
    frame["timestamp"] = time.time()
    telemetry.append(frame)
    sensorData = Sensor_data(frame)
    receivedSensordata.append(sensorData)

    if initialBearing == -1.0:
        initialBearing = sensorData.bearing
        positions.append(Position(0, 0))

    forwardSpeed = driver_logic.stop_and_rotate_on_obstacle(roverController, sensorData)
    currentPosition = reconstructPosition(initialBearing, sensorData.bearing, positions[-1], forwardSpeed)
    positions.append(currentPosition)

    receivedOdometryData.append(reconstructOdometry(receivedSensordata, forwardSpeed))

    logfile.write(json.dumps(frame))
    logfile.flush()


client = mqtt.Client()
roverController = Rover(client)
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(cfg.username, cfg.password)
client.connect(cfg.hostname, cfg.port, cfg.keepalive)
try:
    client.loop_forever()
except KeyboardInterrupt:
    roverController.stop()
    writeToG2oFile(receivedOdometryData)

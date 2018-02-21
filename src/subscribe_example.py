#!/usr/bin/env python3
import json
import time

import paho.mqtt.client as mqtt

import src.config as cfg
from src.rover_commands import Rover
from src.sensor_data import Sensor_data
from src.stopWhenCloseToObstacle import stopIfObstacleWithinThreshold

telemetry = []
f = open("/tmp/test.dat", "a")


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(cfg.topic_telemetry, qos=0)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    frame = json.loads(msg.payload.decode('utf8'))
    frame["timestamp"] = time.time()
    telemetry.append(frame)
    print(frame)
    sensorData = Sensor_data(frame)
    stopIfObstacleWithinThreshold(roverController, sensorData.getNearestDetectedAngleAndDistance()[1])
    print(sensorData.getDetectedDistances())
    f.write(json.dumps(frame))
    f.flush()


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

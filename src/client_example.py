#!/usr/bin/env python3

# !/usr/bin/env python3

import paho.mqtt.client as mqtt

import src.config as cfg
from src.rover_commands import Rover
from time import sleep

def on_connect(client, userdata, flags, rc):
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(cfg.topic_telemetry, qos=0)

client = mqtt.Client()
roverController = Rover(client)
client.username_pw_set(cfg.username, cfg.password)
client.connect(cfg.hostname, cfg.port, cfg.keepalive)
client.on_connect = on_connect
roverController.forward_right(100)
sleep(1.)
roverController.forward_left(100)
sleep(1.)
roverController.turn_left(100)
sleep(1.)
roverController.turn_right(100)

try:
    client.loop_forever()
except KeyboardInterrupt:
    roverController.stop()

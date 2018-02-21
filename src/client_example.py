#!/usr/bin/env python3

import paho.mqtt.publish as publish
import time

payload_start = '{"mode": 0, "command": "E", "speed": 480}'
payload_stop = '{"mode": 0, "command": "F", "speed": 480}'


def send_payload(payload):
    publish.single(topic="rover/1/RoverDriving/control",
                   payload=payload,
                   hostname="bcx-hono.eastus.cloudapp.azure.com",
                   port=1883,
                   auth={'username': "rover1@DEFAULT_TENANT",
                         'password': "hono-rover1"})


send_payload(payload_start)
time.sleep(1.0)
send_payload(payload_stop)

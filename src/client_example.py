#!/usr/bin/env python3

import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe

ROVER_ID = 1
TOPIC_CONTROL = "rover/{:d}/RoverDriving/control".format(ROVER_ID)
TOPIC_TELEMETRY = "rover/{:d}/telemetry".format(ROVER_ID)
HOSTNAME = "bcx-hono.eastus.cloudapp.azure.com"
PORT = 1883
AUTH = {'username': "rover{:d}@DEFAULT_TENANT".format(ROVER_ID),
        'password': "hono-rover{:d}".format(ROVER_ID)}

payload_start = '{"mode": 0, "command": "E", "speed": 480}'
payload_stop = '{"mode": 0, "command": "F", "speed": 480}'


def send_payload(payload):
    publish.single(topic=TOPIC_CONTROL,
                   payload=payload,
                   hostname=HOSTNAME,
                   port=PORT,
                   auth=AUTH)


send_payload(payload_stop)

topics = [TOPIC_TELEMETRY]

m = subscribe.simple(topics, hostname=HOSTNAME, port=PORT, auth=AUTH, retained=False, msg_count=2)
for a in m:
    print(a.topic)
    print(a.payload)

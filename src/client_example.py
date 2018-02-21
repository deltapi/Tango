#!/usr/bin/env python3

import paho.mqtt.publish as publish

import src.config as config

payload_start = '{"mode": 0, "command": "E", "speed": 480}'
payload_stop = '{"mode": 0, "command": "F", "speed": 480}'

def send_payload(payload):
    publish.single(topic=config.topic_control,
                   payload=payload,
                   hostname=config.hostname,
                   port=config.port,
                   auth=config.auth)


send_payload(payload_start)
send_payload(payload_stop)

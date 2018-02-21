import json

import src.config as cfg


class Rover:

    def __init__(self, client):
        self._client = client

    def move_forward(self, speed=480):
        payload = {"mode": 0, "command": "E", "speed": speed}
        self._client.publish(cfg.topic_control, payload=json.dumps(payload), qos=0)

    def stop_(self, speed=480):
        payload = {"mode": 0, "command": "K", "speed": speed}
        self._client.publish(cfg.topic_control, payload=json.dumps(payload), qos=0)

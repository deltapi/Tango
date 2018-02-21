import json

import src.config as cfg


class Rover:

    def __init__(self, client):
        self._client = client

    def move_forward(self, speed=480):
        payload = {"mode": 0, "command": "W", "speed": speed}
        self._client.publish(cfg.topic_control, payload=json.dumps(payload), qos=0)

    def stop(self):
        payload = {"mode": 0, "command": "W", "speed": 0}
        self._client.publish(cfg.topic_control, payload=json.dumps(payload), qos=0)

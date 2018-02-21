import json
import time

import src.config as cfg


class Rover:

    def __init__(self, client, logfile="/tmp/logfile"):
        self._client = client
        self._speed = 100
        self._logfile = open(logfile, 'a')

    def publish(self, payload):
        payload['timestamp'] = time.time()
        self._logfile.write(json.dumps(payload))
        self._logfile.flush()
        self._client.publish(cfg.topic_control, payload=json.dumps(payload), qos=0)

    def forward(self, speed=100):
        payload = {"mode": 0, "command": "W", "speed": speed}
        self.publish(payload)

    def stop(self):
        payload = {"mode": 0, "command": "F", "speed": 0}
        self.publish(payload)

    def forward_left(self, speed=100):
        payload = {"mode": 0, "command": "E", "speed": speed}
        self.publish(payload)

    def forward_right(self, speed=100):
        payload = {"mode": 0, "command": "Q", "speed": speed}
        self.publish(payload)

    def backward(self, speed=100):
        payload = {"mode": 0, "command": "S", "speed": speed}
        self.publish(payload)

    def backward_right(self, speed=100):
        payload = {"mode": 0, "command": "D", "speed": speed}
        self.publish(payload)

    def backward_left(self, speed=100):
        payload = {"mode": 0, "command": "A", "speed": speed}
        self.publish(payload)

    def turn_left(self, speed=100):
        self.stop()
        payload = {"mode": 0, "command": "J", "speed": speed}
        self.publish(payload)

    def turn_right(self, speed=100):
        self.stop()
        payload = {"mode": 0, "command": "K", "speed": speed}
        self.publish(payload)

    def shutdown(self, speed=100):
        payload = {"mode": 0, "command": "R", "speed": speed}
        self.publish(payload)

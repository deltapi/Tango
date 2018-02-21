#!/usr/bin/env python3
import json
import time

import paho.mqtt.client as mqtt

telemetry = []
f = open("/tmp/test.dat", "a")


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("rover/1/telemetry", 0)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # print(msg.topic+" "+str(msg.payload))
    frame = json.loads(msg.payload)
    frame["timestamp"] = time.time()
    telemetry.append(frame)
    print(frame)
    f.write(json.dumps(frame))
    f.flush()


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("rover1@DEFAULT_TENANT", "hono-rover1")

client.connect("bcx-hono.eastus.cloudapp.azure.com", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()

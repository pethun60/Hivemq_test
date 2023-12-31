import paho.mqtt.client as mqtt
import re
from typing import NamedTuple


		
	
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("/temperatur/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" value="+str(msg.payload))
    #print('sensordata ' + str(sensor_data))

	

client = mqtt.Client()
client.username_pw_set(username="peter", password="Peter_Th")
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.1.105", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()

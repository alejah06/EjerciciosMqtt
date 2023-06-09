# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 21:14:25 2023

@author: Alex
"""

import paho.mqtt.client as mqtt
import time

previous_message_time = 0

topic = "topicej5"

def on_connect(client, userdata, flags, rc):
    client.subscribe("topicej5")

def on_message(client, userdata, msg):
    global previous_message_time       

    current_message_time = time.time()
    if previous_message_time != 0:
        wait_time = current_message_time - previous_message_time
        message = msg.payload.decode()
        message1 = f"El topic es {topic} el mensaje es: {message} y el tiempo es {wait_time}"

        time.sleep(int(wait_time))

        client.publish(topic, message1)
    
    previous_message_time = current_message_time

def on_publish(client, userdata, mid):
    print("Mensaje publicado")

if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_publish = on_publish

    client.connect("simba.fdi.ucm.es")

    client.loop_forever()

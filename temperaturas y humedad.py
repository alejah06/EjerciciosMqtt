# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 20:56:49 2023

@author: Alex
"""

import sys
import time
import multiprocessing
import paho.mqtt.client as mqtt

K0 = 20.0
K1 = 30.0


def on_message(client, userdata, message):
    number = float(message.payload.decode())
    
    if K0 < number < K1:
        event.set()

def subscribe_humidity(event):
    client = mqtt.Client()

    client.connect("simba.fdi.ucm.es")
    client.subscribe("humidity")
    
    while True:
        if event.is_set():
            client.loop(timeout = 1.0)
        else:
            client.disconnect()
            break



def subscribe(topic):

    client = mqtt.Client()
    client.on_message = on_message

    client.connect("simba.fdi.ucm.es")
    client.subscribe(topic)

    client.loop_forever()
          
        

if __name__ == "__main__":
    topic1 = "temperature/t1"
    topic2 = "temperature/t2"
    
    event = multiprocessing.Event()
    

    process1 = multiprocessing.Process(target=subscribe, args=(topic1,))
    process2 = multiprocessing.Process(target=subscribe, args=(topic2,))
    process3 = multiprocessing.Process(target=subscribe_humidity, args=(event,))

    process1.start()
    process2.start()
    process3.start()

    process1.join()
    process2.join()
    process3.join()

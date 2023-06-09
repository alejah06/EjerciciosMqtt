# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 20:11:55 2023

@author: Alex
"""

import time
import multiprocessing
import paho.mqtt.client as mqtt

temps1 = []
temps2 = []

def on_message(client, userdata, message):
    number = float(message.payload.decode())
    
    if message.topic == "temperature/t1":
        temps1.append(number)
    elif message.topic == "temperature/t2":
        temps2.append(number)
        

def subscribe(topic):

    client = mqtt.Client()
    client.on_message = on_message

    client.connect("simba.fdi.ucm.es")
    client.subscribe(topic)

    client.loop_forever()
    
def mean(lista):
    return (sum(lista)/(len(lista)))
        

def calcular(intervalo):
    mutex = multiprocessing.Lock()
    while True:
        time.sleep(intervalo)


        if len(temps1) > 0:
            mutex.acquire()
            max_t1 = max(temps1)
            min_t1 = min(temps1)
            mean_t1 = mean(temps1)
            print(f"El máximo de t1 es: {max_t1}, el minimo es {min_t1}, y la media es {mean_t1}")
            temps1.clear()
            mutex.release()

        if len(temps2) > 0:
            mutex.acquire()
            max_t2 = max(temps2)
            min_t2 = min(temps2)
            mean_t2 = mean(temps2)
            print(f"El máximo de t2 es: {max_t2}, el minimo es {min_t2}, y la media es {mean_t2}")
            temps2.clear()
            mutex.release()
            
        if len(temps2) > 0 and len(temps1) > 0:
            mutex.acquire()
            maxt = max(max_t1, max_t2)
            mint = min(min_t1, min_t2)
            meant = mean(mean_t1, mean_t2)
            print(f"El maximo total es: {maxt}, el minimo es {mint}, y la media es {meant}")
            mutex.release()
        
        

if __name__ == "__main__":
    topic1 = "temperature/t1"
    topic2 = "temperature/t2"

    process1 = multiprocessing.Process(target=subscribe, args=(topic1,))
    process2 = multiprocessing.Process(target=subscribe, args=(topic2,))
    process3 = multiprocessing.Process(target=calcular, args=(8,))

    process1.start()
    process2.start()
    process3.start()

    process1.join()
    process2.join()
    process3.join()

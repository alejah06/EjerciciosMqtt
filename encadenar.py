# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 21:29:56 2023

@author: Alex
"""
import time
import multiprocessing
import paho.mqtt.client as mqtt

K0 = 20.0
K1 = 30.0
previous_message_time = 0
topic = "humidity"

def on_message(client, userdata, message):
    global K0
    number = float(message.payload.decode())
    
    if K0 < number:
        event.set()

def on_message_humidity(client, userdata, msg):
    global previous_message_time
    
    current_message_time = time.time()
    if previous_message_time != 0:
        wait_time = current_message_time - previous_message_time
        message = msg.payload.decode()
        message1 = f"El topic es {topic} el mensaje es: {message} y el tiempo es {wait_time}"

        time.sleep(int(wait_time))

        client.publish(topic, message1)
    if wait_time > 1:
        event2.set()
    
    previous_message_time = current_message_time
            
def primo(numero):
    if numero % 2 == 0:
        return False
    else: aux = (numero // 2) -1
    while aux > 1:
        if numero % aux == 0:
            return False
        aux -= 2
    return True


def on_message_numbers(client, userdata, msg):
    global K0
    message = msg.payload.decode()
    if primo(int(message)):
        print(f"primo encontrado: {message}, desconectándose de humidity...")
    K0 = 100000
        
        


def subscribe_humidity(event):
    client = mqtt.Client()
    client.on_message = on_message_humidity

    client.connect("simba.fdi.ucm.es")
    client.subscribe("humidity")
    
    
    while True:
        if event.is_set():
            client.loop(timeout = 1.0)            
        else:
            client.disconnect()
            break

def subscribe_numbers(event):
    client = mqtt.Client()
    client.on_message = on_message_numbers

    client.connect("simba.fdi.ucm.es")
    client.subscribe("numbers")
    
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
    event2 = multiprocessing.Event()
    
    mutex = multiprocessing.Lock()
    

    process1 = multiprocessing.Process(target=subscribe, args=(topic1,))
    process2 = multiprocessing.Process(target=subscribe, args=(topic2,))
    process3 = multiprocessing.Process(target=subscribe_humidity, args=(event,))
    process4 = multiprocessing.Process(target=subscribe_numbers, args=(event2,))
    
    process4.start()
    process1.start()
    process2.start()
    process3.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()
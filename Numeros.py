import paho.mqtt.subscribe as subscribe
import sys


def main(hostname, lista_int, lista_float):
    topic = "numbers"

    msg = subscribe.simple(topic,
                           hostname=hostname)

    number = msg.payload.decode('utf8')
    if int(number) - float(number) == 0:
        int(number)
    else:
        float(number)
    
    if type(number) == float:
        lista_float += [number]
        print(f'Numero {number} añadido a la lista de reales, que ahora contiene:\n')
        print(lista_float)
    if type(number) == int:
        lista_int += [number]
        print(f'Numero {number} añadido a la lista de enteros, que ahora contiene:\n')
        print(lista_int)

if __name__ == "__main__":
    hostname = 'simba.fdi.ucm.es'
    list_int = []
    list_float = []
    if len(sys.argv)>1:
        hostname = sys.argv[1]
    while True:
        main(hostname, list_int, list_float)
        
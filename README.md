Se trata de 5 scripts de python que utilizan el protocolo mqtt para realizar lo pedido en los ejercicios de MQTT.
Numeros se suscribe al canal numbers y estudia si el numero recibido es entero o real para posteriormente guardarlo en una lista y, cada cierto tiempo, mostrar por pantalla los numeros de cada tipo que han ido apareciendo
Temperaturas se suscribe a temperaturas/t1 y a t2 y saca las temperaturas media, máxima y mínima de ambos canales además de la global, cada 8 segundos.
Temperaturas y humedad crea un cliente mqtt que se suscribe a humedad cuando la temperatura recibida esta entre 20 y 30, y se desuscribe cuando la temperatura sale de este rango
Temporizador se suscribe a un topic genérico llamado "topicej5" y calcula el tiempo entre publicaciones, para despues publicar otro mensaje en el tiempo que ha tardado en publicar el anterior con el timepo que ha tardado.
Encadenar se suscribe a t1 y t2, cuando la temperatura recibida llega a mas de 20, se suscribe a humidity, donde realiza el protocolo de temporizador. Si el tiempo de publicacion es mayor a 1, se suscribirá 
a numbers y cuando encuentre un primo se desuscribirá de humidity.

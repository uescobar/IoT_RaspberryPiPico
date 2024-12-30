###
# Programa que enciende en secuencia 4 leds
# material
#  4 leds
#  4 resistencias de 220 ohms
#  cables 
###
from machine import Pin
import utime

# Definicion de objetos
gpio1 = Pin(18, Pin.OUT)
gpio2 = Pin(19, Pin.OUT)
gpio3 = Pin(20, Pin.OUT)
gpio4 = Pin(21, Pin.OUT)

# Definimos un arreglo
a = [gpio1, gpio2, gpio3, gpio4]

# Logica

while True:
     for k in a:
         k.value(1)
         utime.sleep(0.5)
         k.value(0)
         
         
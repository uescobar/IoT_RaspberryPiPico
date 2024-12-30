###
# Programa que enciende un led mediante un pulsador (push button)
# material
#  1 led
#  1 pulsador
#  1 resistencias de 220 ohms
#  1 resistencia de 10 kohms
#  cables 
###

from machine import Pin

led = Pin(21, Pin.OUT)
pulsador = Pin(19, Pin.IN)

while True:
    # variante 1
    #if pulsador.value()==1:
    #    led.value(1)
    #else:
    #    led.value(0)
    
    # variante 2
    led.value(pulsador.value())
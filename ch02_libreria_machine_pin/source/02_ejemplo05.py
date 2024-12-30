###
# Programa que enciende un led mediante
# la informacion que ingresa el usuario
# letra a para encender, b para apagar, z para salir

# material
#  1 led
#  1 resistencias de 220 ohms
#  cables 
###

from machine import Pin

led = Pin(18, Pin.OUT)

continuar = True

while continuar:
    
    letra = input("Digita una letra: ")
    if letra == 'a':
        led.value(1)
    elif letra == 'b':
        led.value(0)
    elif letra == 'z':
        continuar = False
        
print("Fin de programa")
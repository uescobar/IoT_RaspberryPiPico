from machine import Pin
import utime

# Definir el objeto
# gpio = Pin(#gpio, valor)
gpio = Pin(25, Pin.OUT) # Entrada sería Pin.IN

# Caracteristicas del objeto
    # Salida, es 1 o 0
        # gpio.value(0) o bien gpio,off()
        # gpio.value(1) o bien gpio.on()
    # Entrada, es 1 0 0
        # v = gpio.value() para leer el valor

#utime.sleep(# segundos)
#utime.sleep_ms(# milisegundos)
gpio.value(0)
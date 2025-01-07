from machine import Pin
import utime

# utime.sleep(t)
# utime.sleep_ms(t)
# utime.sleep_us(t)

# devuelven el punto de referencia en micro segundos desde que pasa algo
# utime.ticks_ms()
# utime.ticks_us()

# usandolos podemos restarlos y obtener el valor que paso entre una llama y la otra

trig = Pin(19, Pin.OUT)
echo = Pin(18, Pin.IN)

while True:
    trig.value(1)
    utime.sleep_us(10) 
    trig.value(0) #la señal sonora  se envió por 10microsegundos
    
    t1 = utime.ticks_us() # establecemos el punto en el tiempo de referencia, aqui echo vale 0
    while echo.value() == 0:
        t1 = utime.ticks_us() #actualizamos el t1 cuando echo vale 0 y deja de actualizarse cuando echo vale 1
    while echo.value() == 1:
        t2 = utime.ticks_us() #actualizamos y nos quedamos con el ultimo valor cuandfo echo valia 1
    t = t2 - t1 # obtenemos el tiempo que viajó la onda sonora
    d = 17*t/1000 # calculamos la distancia
    print(d, ' cm')
    utime.sleep_ms(500)
        
    
    
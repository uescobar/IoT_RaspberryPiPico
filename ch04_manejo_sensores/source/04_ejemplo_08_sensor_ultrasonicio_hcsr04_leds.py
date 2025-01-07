from machine import Pin
import utime


def distancia():
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
    #print(d, ' cm')
    return d

trig = Pin(19, Pin.OUT)
echo = Pin(18, Pin.IN)

# crear los 4 gpio para los led
gp10 = Pin(10, Pin.OUT)
gp11 = Pin(11, Pin.OUT)
gp12 = Pin(12, Pin.OUT)
gp13 = Pin(13, Pin.OUT)

gp = [gp10, gp11, gp12, gp13]

while True:
    for k in gp:
        di = distancia()
        print(di, ' cm')
        if int(di) >= 3 and int(di) <= 25: 
            t = 10*di
            k.value(1)
            utime.sleep_ms(int(t))
            k.value(0)
    utime.sleep_ms(500)
        
    
    
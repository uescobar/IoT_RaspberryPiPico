import dht
from machine import Pin
import utime

dht11 = dht.DHT11(Pin(18))

while True:
    utime.sleep(1) 
    dht11.measure()
    t = dht11.temperature()
    h = dht11.humidity()
    print('T = ', t, ', H =', h)
       
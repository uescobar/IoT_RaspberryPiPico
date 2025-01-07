from machine import ADC, Pin
import utime

led1 = Pin(18, Pin.OUT)
led2 = Pin(19, Pin.OUT)
led3 = Pin(20, Pin.OUT)
led4 = Pin(21, Pin.OUT)

leds = [led1, led2, led3, led4]
adc = ADC(2)




while True:
   for k in leds:
       tiempo = 50 + int(adc.read_u16()/327)
       k.value(1)
       utime.sleep_ms(tiempo)
       k.value(0)
       
       
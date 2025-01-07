from machine import ADC, Pin
import utime

ldr = ADC(0)
led = Pin(18, Pin.OUT)

while True:
    valor = ldr.read_u16()
    print(valor)
    if valor >= 30000:
        led.value(0)
    else:
        led.value(1)
        
    utime.sleep_ms(500)
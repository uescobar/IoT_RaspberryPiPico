from machine import ADC
import utime

adc = ADC(2) # GPIO 28, pin 32

while True:
    valor = adc.read_u16()
    voltaje = valor*3.3/65535
    print(valor, ' ', voltaje)
    
    utime.sleep_ms(200)

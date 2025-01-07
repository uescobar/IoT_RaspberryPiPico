from machine import ADC
import utime

ldr = ADC(0)

while True:
    valor = ldr.read_u16()
    print(valor)
    utime.sleep_ms(500)
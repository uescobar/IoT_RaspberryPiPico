from machine import ADC
import utime

sensor = ADC(4) #es un adc interno unicamente para el sensor de temperatura

while True:
    valor = sensor.read_u16()
    voltaje = valor * 3.3 /65535 # poque es de 16 bits
    temp = 27-(voltaje-0.706)/0.001721
    print(temp, ' Centigrados')
    utime.sleep_ms(500)
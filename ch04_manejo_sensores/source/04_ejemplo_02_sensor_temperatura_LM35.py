# primero mostar la hoja de especificaciones de LM35 y como es la configuracion de sus patitas
# el propósito de este codigo es comparar la lectura de LM35 con el sensor interno de temperatura


from machine import ADC
import utime

sensor = ADC(4) #es un adc interno unicamente para el sensor de temperatura
lm35 = ADC(1) #GP27 es el ADC1


while True:
    valor = sensor.read_u16() # sensor interno
    valor2 = lm35.read_u16() # sensor LM35
    voltaje = valor * 3.3 /65535 # poque es de 16 bits
    voltaje2 = valor2 * 3.3 / 65535 # poque es de 16 bits
    temp = 27-(voltaje-0.706)/0.001721
    
    
    # temp2 = 100*voltaje2 # usar con lm35
    temp2 = (voltaje2 - 0.55)*100 # usar con lm36gz
    
    print('Temp intern: ', temp, ', Temp lm35', temp2)
    utime.sleep_ms(500)
from machine import ADC,Pin
import utime

led = Pin(18, Pin.OUT)
adc = ADC(2)

# el rango del ADC va de 0 a 65535, así que
# dividimos 65535 / 200 y da 327
# y si dividimos 65535 /327 va a dar 200 que es
# el valor maximo que queremos sumar al tiempo



while True:
    
    valor = adc.read_u16()
    # tiempo 50 ms + otros milisegundos calculados
    tiempo = 50 + int(valor/327)
    led.value(1) # primer momento comentado, segundo momento descomentado
    # print(int(tiempo)) # primer momento descomentado, segundo momento comentado
    # utime.sleep_ms(200) # primer momento descomentado, segundo momento comentado 
    
    utime.sleep_ms(tiempo) # primer momento comentado, segundo momento descomentado
    led.value(0) # primer momento comentado, segundo momento descomentado
    utime.sleep_ms(int(tiempo)) # primer momento comentado, segundo momento descomentado
    

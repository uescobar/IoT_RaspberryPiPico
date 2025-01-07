# El potenciometro varía de 0 a 65535
# y el servo varía de 0 a 180

from machine import PWM,Pin, ADC
import utime

pwm = PWM(Pin(7))
# Los servomotores tienen un tiempo de respuesta de 20 milisegundos para su operacion
pwm.freq(50) # lafrecuencia de 50 equivale a 20 milisegundos
adc = ADC(2) # GP28 es ADC2, GP27 es ADC1 y GP26 es el ADC0

while True:
    # se lee de 0 a 65535, para convertirlo hacemos 65535/180=364.08
    angulo = int(adc.read_u16()/364) # Se divide entre 364 para que nos de un valor entre 0 y 180
    print(angulo)
    #calculamos el valor del duty cycle
    dc = 1638.375 + 36.4*angulo
    pwm.duty_u16(int(dc))        
     



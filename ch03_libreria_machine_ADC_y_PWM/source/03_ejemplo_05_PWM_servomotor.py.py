from machine import PWM,Pin

pwm = PWM(Pin(7)) # probar con 18

pwm.freq(50) #frecuencia comun de trabajo del servo
             # es decir el periodo T=20ms
    
continuar = True

while continuar:
    angulo = input('Digite el angulo del servo: ')
    if angulo == 'z':
        pwm.deinit() # liberamos el pwm
        continuar=False
    else:
        #calculamos el valor del duty cycle
        dc = 1638.375 + 36.4*int(angulo)
        pwm.duty_u16(int(dc))        

print('Fin de programa')
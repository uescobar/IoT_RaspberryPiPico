from machine import PWM,Pin

pwm = PWM(Pin(18)) # gpio18
pwm.freq(500) #T=2ms, un periodo de 2ms

continuar = True

while continuar:
    a = input('Digite un valor de 0 a 100: ')
    if a == 'z':
        continuar = False
    else:
        # recordemos que el dc va de 0 a 65535
        # se debe realizar el calculo multiplicando el valor por 655, valor aproximado
        pwm.duty_u16(int(a)*655)
        
pwm.deinit()
print('Fin de programa')
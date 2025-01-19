from ssd1306 import SSD1306_I2C
from machine import I2C,Pin
import utime
import math

i2c = I2C(0,scl=Pin(1),sda=Pin(0),freq=400000)
oled = SSD1306_I2C(128,64,i2c)

#ubicarse en el centro de la pantalla
x0=64
y0=32

# tiene que ser menor a 32
r=10

# necesitamos ángulos de 360 grados para gradicar la circunferencia
# como la pantalla es chica, tomaremos de 0 a 90
for k in range (271): # hasta 90 e sun giro, 180 dos giros, ... 271 tres giros
    x=x0+int(r*math.cos(4*k*2*math.pi/360)) # se usan radianes
    y=y0-int(r*math.sin(4*k*2*math.pi/360)) # se usan radianes, y es resta porque y crece hacia abajo
    # r=(181/180)*r # el valor de r crecerá un poco cada vez que itera
    r=(271/270)*r # el valor de r crecerá un poco cada vez que itera
    oled.pixel(x,y,1)
    oled.show()


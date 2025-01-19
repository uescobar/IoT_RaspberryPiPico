from ssd1306 import SSD1306_I2C
from machine import I2C,Pin
import utime
import math

i2c = I2C(0,scl=Pin(1),sda=Pin(0),freq=400000)
oled = SSD1306_I2C(128,64,i2c)

# En el eje x debemos tener radianes, pero en lugar de eso
# tendremos ángulo, normalmente deberia de ser de 0 a 360 grados
# pero debido a la limitacion de las dimensiones de la pantalla,
# lo que tendremos será de 0 a 128 puntos para graficar,
# así que 360 / 2 = 180, por lo que aun tomando escala a la mitad
# en ancho de la pantalla no nos alcanza, así que lo volvemos a
# dividir entre dos 180 / 2 = 90, por lo que el eje x va a ir de
# 0 a 90, pero en el argumento de sin(x) lo vamos a multiplicar por 4

# en el eje y, tenemos hasta 64 puntos, por lo que el eje x lo vamos
# poner en el punto 32, que es la mitad de la pantalla y trabajaremos
# con 30 unidades hacia arriba y 30 unidades hacia abajo. Por lo que, 
# para al obtener el valor de la función sin(x), lo vamos a multiplicar
# por 30. 

# valores iniciales de x y y para establecer los ejes
y0=32 # es el valor inicial de y para que 0 se desplaze 32 puntos
x0 = 19 # este eje usa 90 puntos de 128, quedando 38 puntos libres, la mitad es 19, para centrarlo
# graficando los valores de y
for x in range (91): # se usa 91 para que sea de 0 a 90
    # ya multiplicado va de 0 a 360 y se convierte a radianes,
    # y se multiplica por 30 para que vaya de -30 a 30
    y = -int(30*math.sin(4*x*2*math.pi/360)) # se pone negativo porque y aumenta hacia abajo de la pantalla
    # primero graficar puntos (descomentar)
    oled.pixel(x+x0,y+y0,1) # el uno significa encender el pixel
    # segundo graficar lineas (comentar)
    #oled.line(x+x0,y0, x+x0,y+y0,1)
    oled.show()
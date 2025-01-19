from ssd1306 import SSD1306_I2C
from machine import I2C,Pin
import utime

i2c = I2C(0,scl=Pin(1),sda=Pin(0),freq=400000)
oled = SSD1306_I2C(128,64,i2c)

while True:
    oled.text("Hola",0,0,1)
    oled.text("Raspberry",0,15,1)
    oled.text("Pi Pico",0,30,1)
    oled.show()
    utime.sleep(1)
    oled.fill(0)
    oled.show()
    utime.sleep(0.5)
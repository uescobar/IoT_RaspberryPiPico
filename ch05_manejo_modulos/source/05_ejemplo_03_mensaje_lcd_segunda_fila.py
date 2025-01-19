from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd
import utime

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)

lcd = I2cLcd(i2c, 39, 2, 16)

while True:
    lcd.move_to(0,1)
    lcd.putstr("Hola Mundo")
    utime.sleep(1)
    lcd.clear()
    utime.sleep(1)
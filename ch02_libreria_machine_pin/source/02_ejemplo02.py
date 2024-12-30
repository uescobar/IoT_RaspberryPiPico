from machine import Pin
import utime 

gpio18 = Pin(18, Pin.OUT)
gpio19 = Pin(19,Pin.OUT)

while True:
  gpio18.value(1)
  gpio19.value(0)
  utime.sleep(1)
  
  gpio18.value(0)
  gpio19.value(1)
  utime.sleep(0.5)
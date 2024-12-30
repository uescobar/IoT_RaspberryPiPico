from machine import Pin
import utime 

gpio1 = Pin(18, Pin.OUT)

while True:
  gpio1.value(1)
  utime.sleep(1)
  gpio1.value(0)
  utime.sleep(0.5)
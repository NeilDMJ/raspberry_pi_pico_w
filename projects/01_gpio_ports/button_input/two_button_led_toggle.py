from machine import Pin
import time

pin = Pin(12, Pin.OUT)
pin2 = Pin(13, Pin.OUT)

b1 = Pin(16, Pin.IN, Pin.PULL_UP)
b2 = Pin(18, Pin.IN, Pin.PULL_UP)

while True:
    if b1.value() == 0:
        pin.toggle()
    if b2.value() == 0:
        pin2.toggle()
    time.sleep_ms(300)

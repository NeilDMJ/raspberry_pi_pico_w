from machine import UART, Pin
import time

print("Uso de la UART!")

#uart = UART(0, baudrate=9600, bits=8, parity=None, stop=1, tx=Pin(0), rx=Pin(1))
uart = UART(0, 9600, tx=Pin(16), rx=Pin(17))
uart.write("Uso de la UART!")

led_verde = Pin(14,Pin.OUT)
led_rojo = Pin(15,Pin.OUT)

while True:
    if uart.any():
        accion_bin = uart.read()
        print(accion_bin)
        if accion_bin == "1":
            led_verde.toggle();
        elif accion_bin == "2":
            led_rojo.toggle();
    
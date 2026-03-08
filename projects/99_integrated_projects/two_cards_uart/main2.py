from machine import UART, Pin
import time

print("Uso de la UART!")

#uart = UART(0, baudrate=9600, bits=8, parity=None, stop=1, tx=Pin(0), rx=Pin(1))
uart = UART(0, 9600, tx=Pin(16),rx=Pin(17))
uart.write("Uso de la UART!")

boton_verde = Pin(14, Pin.OUT, Pin.PULL_DOWN)
boton_rojo = Pin(15, Pin.OUT, Pin.PULL_DOWN)

while True:
    if boton_verde.value() == 0:
        uart.write(str(1).encode('utf-8'))
        print(uart)
    elif boton_rojo.value() == 0:
        uart.write(str(2).encode('utf-8'))
        print(uart)


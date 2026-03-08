import time
import display
import uart_manager

pos = 0

while True:
    digitos = display._digitos(display.contador)
    display._mostrar(pos, digitos[pos])
    time.sleep_ms(5)
    pos = (pos + 1) % 4
from machine import Pin
import time

pins = [Pin(12, Pin.OUT), Pin(14, Pin.OUT), Pin(15, Pin.OUT), Pin(16, Pin.OUT)]


def mostrar_en_binario(numero):
    bin_str = f"{numero:04b}"
    for i in range(4):
        valor_bit = int(bin_str[i])
        pins[i].value(valor_bit)


try:
    while True:
        for contador in range(9):
            mostrar_en_binario(contador)
            print(f"Decimal: {contador} -> Binario: {contador:04b}")
            time.sleep(0.5)

except KeyboardInterrupt:
    for p in pins:
        p.off()

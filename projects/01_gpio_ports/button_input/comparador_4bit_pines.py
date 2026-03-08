from machine import Pin
from utime import sleep


Op1 = [Pin(i+2, Pin.IN, Pin.PULL_DOWN) for i in range(4)] #primer arreglo de pines
Op2 = [Pin(i+6, Pin.IN, Pin.PULL_DOWN) for i in range(4)] #segundo arreglo de pines

salida = [Pin(21, Pin.OUT), Pin(16, Pin.OUT), Pin(18, Pin.OUT)] #pin de salida

def comparar_valor(op1,op2):
    resultado = 0
    # Comparar desde el bit más significativo (MSB) al menos significativo (LSB)
    for i, j in zip(reversed(op1), reversed(op2)):
        if i.value() != j.value():
            if i.value() > j.value():
                resultado = 1
            elif i.value() < j.value():
                resultado = 2
            break
    return resultado

while True:
    res = comparar_valor(Op1, Op2)
    if res == 1:
        salida[0].value(1)
        salida[1].value(0)
        salida[2].value(0)
    elif res == 2:
        salida[0].value(0)
        salida[1].value(1)
        salida[2].value(0)
    else:
        salida[0].value(0)
        salida[1].value(0)
        salida[2].value(1)
    sleep(0.5)

from machine import Pin
import time

SEG = [Pin(p, Pin.OUT) for p in (2, 3, 4, 5, 6, 7, 8)]
DIG = [Pin(p, Pin.OUT) for p in (9, 10, 11, 12)]


TABLA = [
    [1,1,1,1,1,1,0],  # 0
    [0,1,1,0,0,0,0],  # 1
    [1,1,0,1,1,0,1],  # 2
    [1,1,1,1,0,0,1],  # 3
    [0,1,1,0,0,1,1],  # 4
    [1,0,1,1,0,1,1],  # 5
    [1,0,1,1,1,1,1],  # 6
    [1,1,1,0,0,0,0],  # 7
    [1,1,1,1,1,1,1],  # 8
    [1,1,1,1,0,1,1],  # 9
]


btn_up   = Pin(13, Pin.IN, Pin.PULL_UP)
btn_down = Pin(14, Pin.IN, Pin.PULL_UP)
btn_set  = Pin(15, Pin.IN, Pin.PULL_UP)
btn_rst  = Pin(16, Pin.IN, Pin.PULL_UP)


contador = 0

# Marca de tiempo de la última pulsación válida por botón
_t_up   = 0
_t_down = 0
_t_set  = 0
_t_rst  = 0

DEBOUNCE_MS = 200


#ISR
def handle_up(pin):
    global contador, _t_up
    ahora = time.ticks_ms()
    if time.ticks_diff(ahora, _t_up) < DEBOUNCE_MS:
        return
    _t_up = ahora
    contador = 0 if contador >= 1000 else contador + 1

def handle_down(pin):
    global contador, _t_down
    ahora = time.ticks_ms()
    if time.ticks_diff(ahora, _t_down) < DEBOUNCE_MS:
        return
    _t_down = ahora
    contador = 1000 if contador <= 0 else contador - 1

def handle_set(pin):
    global contador, _t_set
    ahora = time.ticks_ms()
    if time.ticks_diff(ahora, _t_set) < DEBOUNCE_MS:
        return
    _t_set = ahora
    contador = 500

def handle_rst(pin):
    global contador, _t_rst
    ahora = time.ticks_ms()
    if time.ticks_diff(ahora, _t_rst) < DEBOUNCE_MS:
        return
    _t_rst = ahora
    contador = 0


# Asociar cada botón con su handler en flanco de bajada
btn_up.irq(trigger=Pin.IRQ_FALLING,   handler=handle_up)
btn_down.irq(trigger=Pin.IRQ_FALLING, handler=handle_down)
btn_set.irq(trigger=Pin.IRQ_FALLING,  handler=handle_set)
btn_rst.irq(trigger=Pin.IRQ_FALLING,  handler=handle_rst)


def _apagar():
    for d in DIG:
        d.value(1)   # dígito inactivo 

def _mostrar(posicion, valor):
    """enciende un display con su valor correspondiente"""
    _apagar()
    for i, seg in enumerate(SEG):
        seg.value(TABLA[valor][i])
    DIG[posicion].value(0)   # activar dígito

def _digitos(n):
    """divide n en unidades, decenas, centenas, millares."""
    return [
        n         % 10,
        (n // 10) % 10,
        (n // 100) % 10,
        (n // 1000) % 10,
    ]


pos = 0

while True:
    digitos = _digitos(contador)
    _mostrar(pos, digitos[pos])
    time.sleep_ms(5)
    pos = (pos + 1) % 4

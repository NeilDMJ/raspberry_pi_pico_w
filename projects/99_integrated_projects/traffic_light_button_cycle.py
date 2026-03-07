from machine import Pin
import time

r1 = Pin(0, Pin.OUT)
a1 = Pin(1, Pin.OUT)
v1 = Pin(2, Pin.OUT)

r2 = Pin(11, Pin.OUT)
a2 = Pin(13, Pin.OUT)
v2 = Pin(14, Pin.OUT)

button = Pin(17, Pin.IN, Pin.PULL_UP)

leds = [r1, a1, v1, r2, a2, v2]

tiempos = [2, 1, 1, 2, 1, 1]

combinaciones = {
    0: [1, 0, 0, 0, 0, 1],
    1: [1, 0, 0, 0, 0, "pd"],
    2: [1, 0, 0, 0, 1, 0],
    3: [0, 0, 1, 1, 0, 0],
    4: [0, 0, "pd", 1, 0, 0],
    5: [0, 1, 0, 1, 0, 0],
}


def base():
    '''Regresamos el estado base de los pines'''
    r1.value(1)
    a1.value(0)
    v1.value(0)
    r2.value(0)
    a2.value(0)
    v2.value(1)


def blink(pin, duration_s):
    '''Funcion que nos ayuda a hacer el parpadeo'''
    start = time.ticks_ms()
    while time.ticks_diff(time.ticks_ms(), start) < int(duration_s * 1000):
        pin.value(0)
        time.sleep(0.3)
        pin.value(1)
        time.sleep(0.3)
    pin.value(0)


def iluminar(estado, tiempo):
    '''Funcion principal que lleva acabo el encendido de los leds'''
    combinacion = combinaciones[estado]
    parpa = None
    for i in range(len(combinacion)):
        if combinacion[i] == "pd":
            parpa = leds[i]
            leds[i].value(0)
        else:
            leds[i].value(combinacion[i])
    if parpa:
        blink(parpa, tiempo)
    else:
        time.sleep(tiempo)


def ciclo_semaforos():
    '''Hace el ciclo de los semaforos'''
    for i in range(len(tiempos)):
        iluminar(i, tiempos[i])


base()

while True:
    if button.value() == 1:
        while button.value() == 1:
            if button.value() == 0:
                base()
                time.sleep(0.1)
                break
            ciclo_semaforos()
            base()
            time.sleep(0.1)
    else:
        base()
        time.sleep(0.1)

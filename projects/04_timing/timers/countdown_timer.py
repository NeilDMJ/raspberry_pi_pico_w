from machine import Timer

# variables globales para el temporizador
contador = 5
tiempo_inicial = contador
tim = Timer(-1)

def temporizador_descendente(timer):
    global contador
    if contador > 0:
        contador -= 1
    else:
        timer.deinit()  # Detener el temporizador cuando llegue a 0

tim.init(period=1000, mode=Timer.PERIODIC, callback=temporizador_descendente)


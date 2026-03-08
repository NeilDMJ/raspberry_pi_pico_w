"""
Módulo para el manejo de botones con debounce
"""
from machine import Pin
import time

# Configuración de botones con pull-up
btn_up   = Pin(14, Pin.IN, Pin.PULL_UP)
btn_down = Pin(15, Pin.IN, Pin.PULL_UP)
btn_set  = Pin(16, Pin.IN, Pin.PULL_UP)
btn_rst  = Pin(17, Pin.IN, Pin.PULL_UP)

# Estado del sistema: "IDLE", "RUNNING", "PAUSED"
estado = "IDLE"

# Tiempo en segundos (0-5999, máximo 99:59)
tiempo_segundos = 0

# Marca de tiempo de la última pulsación válida por botón (para debounce)
_t_up   = 0
_t_down = 0
_t_set  = 0
_t_rst  = 0

# Tiempo de debounce en milisegundos
DEBOUNCE_MS = 200

# Marca de tiempo para avance de contador en RUNNING
_t_tick = time.ticks_ms()


# ISR (Interrupt Service Routines)
def handle_up_1(pin):
    """Handler para incrementar el tiempo en 1 segundo (+1 botón)"""
    global tiempo_segundos, _t_up, estado
    
    # Solo funciona en IDLE o PAUSED
    if estado != "IDLE" and estado != "PAUSED":
        return
    
    ahora = time.ticks_ms()
    if time.ticks_diff(ahora, _t_up) < DEBOUNCE_MS:
        return
    _t_up = ahora
    
    # Incrementar 1 segundo con límite de 5999 (99:59)
    if tiempo_segundos < 5999:
        tiempo_segundos += 1


def handle_up_10(pin):
    """Handler para incrementar el tiempo en 10 segundos (+10 botón)"""
    global tiempo_segundos, _t_down, estado
    
    # Solo funciona en IDLE o PAUSED
    if estado != "IDLE" and estado != "PAUSED":
        return
    
    ahora = time.ticks_ms()
    if time.ticks_diff(ahora, _t_down) < DEBOUNCE_MS:
        return
    _t_down = ahora
    
    # Incrementar 10 segundos con límite de 5999 (99:59)
    tiempo_segundos = min(tiempo_segundos + 10, 5999)


def handle_begin(pin):
    """Handler para iniciar/reanudar el temporizador (Inicio botón)"""
    global estado, _t_set, tiempo_segundos, _t_tick
    
    ahora = time.ticks_ms()
    if time.ticks_diff(ahora, _t_set) < DEBOUNCE_MS:
        return
    _t_set = ahora
    
    # Ignorar si ya está corriendo
    if estado == "RUNNING":
        return
    
    # Ignorar si el tiempo es 0
    if tiempo_segundos == 0:
        return
    
    # Cambiar a RUNNING (desde IDLE o PAUSED)
    estado = "RUNNING"
    _t_tick = ahora


def handle_rst_pause(pin):
    """Handler para reset/pausa (Rst/Pausa botón)"""
    global estado, _t_rst, tiempo_segundos
    
    ahora = time.ticks_ms()
    if time.ticks_diff(ahora, _t_rst) < DEBOUNCE_MS:
        return
    _t_rst = ahora
    
    if estado == "IDLE":
        # Reset: poner tiempo en 0
        tiempo_segundos = 0
        
    elif estado == "RUNNING":
        # Pausa: detener pero mantener el tiempo
        estado = "PAUSED"
        
    elif estado == "PAUSED":
        # Reset desde pausa: poner tiempo en 0 y volver a IDLE
        tiempo_segundos = 0
        estado = "IDLE"


# Asociar cada botón con su handler en flanco de bajada
btn_up.irq(trigger=Pin.IRQ_FALLING,   handler=handle_up_1)
btn_down.irq(trigger=Pin.IRQ_FALLING, handler=handle_up_10)
btn_set.irq(trigger=Pin.IRQ_FALLING,  handler=handle_begin)
btn_rst.irq(trigger=Pin.IRQ_FALLING,  handler=handle_rst_pause)


# Funciones de acceso y control
def get_tiempo_segundos():
    """Obtiene el tiempo actual en segundos"""
    return tiempo_segundos


def set_tiempo_segundos(valor):
    """Establece el tiempo en segundos"""
    global tiempo_segundos, _t_tick
    tiempo_segundos = max(0, min(valor, 5999))
    _t_tick = time.ticks_ms()


def get_estado():
    """Obtiene el estado actual del sistema"""
    return estado


def set_estado(nuevo_estado):
    """Establece el estado del sistema"""
    global estado, _t_tick
    if nuevo_estado in ["IDLE", "RUNNING", "PAUSED"]:
        estado = nuevo_estado
        _t_tick = time.ticks_ms()


def actualizar_tiempo():
    """Actualiza el contador cada 1s cuando el estado es RUNNING (conteo descendente)."""
    global _t_tick, tiempo_segundos, estado

    ahora = time.ticks_ms()

    # Si no está corriendo, re-sincronizar referencia de tiempo
    if estado != "RUNNING":
        _t_tick = ahora
        return

    # Avanzar de segundo en segundo para evitar saltos por jitter
    while time.ticks_diff(ahora, _t_tick) >= 1000:
        if tiempo_segundos > 0:
            tiempo_segundos -= 1
            _t_tick = time.ticks_add(_t_tick, 1000)
        else:
            # Llegó a 00:00
            estado = "IDLE"
            _t_tick = ahora
            break

"""
Programa principal del temporizador con display de 7 segmentos
Importa la lógica del display y el manejo de botones de módulos separados
"""
from machine import Pin
import time
import display
import buttons
import sound

# Pin de salida adicional (si se necesita)
salida = Pin(0, Pin.OUT)

# Posición actual del dígito a mostrar
pos = 0

# Estado anterior para detectar transiciones y disparar sonido una sola vez
estado_anterior = buttons.get_estado()

# Loop principal: multiplexación del display
while True:
    # Actualizar contador (1 segundo) si está corriendo
    buttons.actualizar_tiempo()

    estado_actual = buttons.get_estado()

    # Pin de salida en alto solo durante RUNNING
    if estado_actual == "RUNNING":
        salida.value(1)
    else:
        salida.value(0)

    # Obtener el valor actual del contador desde el módulo de botones
    valor_contador = buttons.get_tiempo_segundos()

    # Sonar una sola vez al detenerse por llegar a 00:00
    if (
        estado_anterior == "RUNNING"
        and estado_actual == "IDLE"
        and valor_contador == 0
    ):
        sound.play_three_notes()

    estado_anterior = estado_actual
    
    # Dividir el contador en dígitos individuales
    digitos_lista = display.digitos(valor_contador)
    
    # Mostrar el dígito en la posición actual
    display.mostrar(pos, digitos_lista[pos])
    
    # Esperar un breve momento
    time.sleep_ms(5)
    
    # Avanzar a la siguiente posición (0→1→2→3→0...)
    pos = (pos + 1) % 4
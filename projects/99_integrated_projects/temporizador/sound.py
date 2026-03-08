"""
Sonido simple para buzzer: secuencia de 3 notas.
"""
from machine import Pin, PWM
from utime import sleep_ms

BUZZER_PIN = 22
VOLUME = 1000

buzzer = PWM(Pin(BUZZER_PIN))

def _tone(freq, ms):
    buzzer.freq(freq)
    buzzer.duty_u16(VOLUME)
    sleep_ms(ms)
    buzzer.duty_u16(0)


def play_three_notes():
    """Reproduce 3 notas cortas."""
    _tone(523, 150)  # C5
    sleep_ms(50)
    _tone(659, 150)  # E5
    sleep_ms(50)
    _tone(784, 200)  # G5


def stop_sound():
    """Apaga el buzzer."""
    buzzer.duty_u16(0)
from machine import SPI, Pin
import time

matriz =SPI(0, 10000, sck = Pin(6), mosi=Pin(3), miso=Pin(4)) #sck terminal para reloj
cs_matriz = Pin(5, Pin.OUT)
cs_matriz.value(1) #esclavo inactivo

def Send(registro, value):
    cs_matriz.value(0)
    matriz.write(bytearray([registro, value]))
    cs_matriz.value(1)

def Configure():
    Send(0x09, 0) #Sin decodificador de 7seg
    Send(0x0A, 8) #Intensidad media (0 a 15)
    Send(0x0B, 7) # Se usarán los 8 renglones (0 al 7)
    Send(0x0C, 1) # Inicia apagado 

def Paint(imagen):
    for i in range(8):
        Send(i + 1, imagen[i])

# Círculos concéntricos que crecen desde el centro
circulo1 = [
    0b00000000,
    0b00000000,
    0b00000000,
    0b00011000,
    0b00011000,
    0b00000000,
    0b00000000,
    0b00000000
]

circulo2 = [
    0b00000000,
    0b00000000,
    0b00111100,
    0b00100100,
    0b00100100,
    0b00111100,
    0b00000000,
    0b00000000
]

circulo3 = [
    0b00000000,
    0b01111110,
    0b01000010,
    0b01000010,
    0b01000010,
    0b01000010,
    0b01111110,
    0b00000000
]

circulo4 = [
    0b11111111,
    0b10000001,
    0b10000001,
    0b10000001,
    0b10000001,
    0b10000001,
    0b10000001,
    0b11111111
]

circulos = [circulo1, circulo2, circulo3, circulo4]

Configure()  # Configurar la matriz de LED una vez

while True:
    for circulo in circulos:
        Paint(circulo)
        time.sleep(0.2)  # Pausa entre cada círculo
    for circulo in reversed(circulos):
        Paint(circulo)
        time.sleep(0.2)  # Pausa entre cada círculo
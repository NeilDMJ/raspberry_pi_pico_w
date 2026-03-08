"""
Módulo para el control del display de 7 segmentos de 4 dígitos
"""
from machine import Pin

# Configuración de pines para los segmentos (a-g)
SEG = [Pin(p, Pin.OUT) for p in (2, 3, 4, 5, 6, 7, 8)]
# Configuración de pines para los dígitos
DIG = [Pin(p, Pin.OUT) for p in (9, 10, 11, 12)]

# Tabla de segmentos para cada dígito (0-9)
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

def apagar():
    """Apaga todos los dígitos del display"""
    for d in DIG:
        d.value(1)   # dígito inactivo 

def mostrar(posicion, valor):
    """Enciende un display con su valor correspondiente
    
    Args:
        posicion: Posición del dígito (0-3)
        valor: Valor a mostrar (0-9)
    """
    apagar()
    for i, seg in enumerate(SEG):
        seg.value(TABLA[valor][i])
    DIG[posicion].value(0)   # activar dígito

def digitos(n):
    """Convierte segundos totales a formato MMSS.
    
    Args:
        n: Tiempo total en segundos (0-5999)
        
    Returns:
        Lista con [u_seg, d_seg, u_min, d_min]
    """
    minutos = n // 60
    segundos = n % 60

    return [
        segundos % 10,
        (segundos // 10) % 10,
        minutos % 10,
        (minutos // 10) % 10,
    ]

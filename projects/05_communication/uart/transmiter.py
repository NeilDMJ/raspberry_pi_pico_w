#enviar serialmente a raspberry pi pico
import serial

def enviar_datos(datos):
    puerto_serial = '/dev/ttyUSB0'  
    velocidad_baudio = 9600

    try:
        # Abrir el puerto serial
        ser = serial.Serial(puerto_serial, velocidad_baudio)

        # Enviar los datos como bytes
        ser.write(datos.encode('utf-8'))

        # Cerrar el puerto serial
        ser.close()
        print("Datos enviados correctamente.")
    except Exception as e:
        print(f"Error al enviar datos: {e}")

# enviar numeros de hasta 4 digitos leidos de consola  
if __name__ == "__main__":
    while True:
        print("Ingrese dos numeros de hasta 3 dígitos y una operacion basica(o 'salir' para terminar): ")
        numero1 = input("Número 1: ")
        operacion = input("Operación (+, -, *, /): ")
        numero2 = input("Número 2: ")
        entrada = f"{numero1}{operacion}{numero2}"
        print(f"Entrada: {entrada}")
        if entrada.lower() == 'salir':
            break
        elif len(numero1) <= 3 and len(numero2) <= 3 and operacion in ['+', '-', '*', '/']:
            enviar_datos(entrada)
        else:
            print("Entrada no válida. Por favor, ingrese dos números de hasta 3 dígitos y una operación válida (+, -, *, /).")
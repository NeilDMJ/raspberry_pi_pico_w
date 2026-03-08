import time
from machine import Pin, UART

connection = UART(0, baudrate=9600, tx=Pin(16), rx=Pin(17))

def receive_data():
    if connection.any():
        data = connection.read()
        print("Received:", data)

def convert_data(data):
    data_arr = data.decode().split(',')
    if len(data_arr) == 4:
        try:
            return [int(x) for x in data_arr]
        except ValueError:
            print("Invalid data format")
    else:
        print("Data should contain 4 comma-separated values")
    return None 


from machine import Pin, PWM, ADC
import time

pwm0 = PWM(Pin(0), freq=100, duty_u16=0) # pwm0 inicia al 50 %
pot = ADC(0)

while True:
    valor = pot.read_u16()
    pwm0.duty_u16(valor)
    print(valor)
    time.sleep_ms(20)
    


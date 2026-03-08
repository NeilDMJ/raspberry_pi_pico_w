from machine import Pin, Timer

led = Pin(20, Pin.OUT)
button = Pin(21, Pin.IN, Pin.PULL_DOWN)

counter = 0
debounce_timer = None  # Debounce timer object

def button_pressed(pin):
    global counter, debounce_timer
    if debounce_timer is None:
        counter += 1

        print("Button pressed! Counter:", counter)
        led.toggle()  # Toggle the LED state
        # Start debounce timer
        debounce_timer = Timer(-1)  # Create a timer object
        debounce_timer.init(mode=Timer.ONE_SHOT, period=200, callback=debounce_callback)

def debounce_callback(timer):
    global debounce_timer
    debounce_timer = None  # Reset debounce timer

button.irq(trigger=Pin.IRQ_RISING, handler=button_pressed)

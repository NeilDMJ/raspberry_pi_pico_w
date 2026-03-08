import array as arr
import micropython

registros = arr.array('i',[
    0x40014000,             # IO_BANK0_BASE
    0xd0000000                 # SIO_BASE
    ])

@micropython.asm_thumb
def blink(r0):
    b(START)
    label(config_led)
    ldr(r1, [r0, 0])        # IO_BANK0_BASE
    mov(r2, 5)              # Function 5, SIO
    mov(r3, 0xc8)           # 25 * 8 = 200 = 0xC8 (offset para GPIO25_CTRL)
    add(r1, r1, r3)         # IO_BANK0_BASE + offset GPIO25
    str(r2, [r1, 0x04])     # GPIO25_CTRL
    ldr(r1, [r0, 4])        # dirección base de SIO
    mov(r2, 1)
    lsl(r2, r2, 25)         # 1 << 25 para GPIO25
    str(r2, [r1, 0x24])     # GPIO output enable
    bx(lr)
   
    label(delay)
    mov(r3, 1)
    lsl(r3, r3, 25)         # Número muy grande
    label(loop)
    sub (r3, 1)             # resta 1 del registro r0
    bne (loop)
    bx(lr)
   
    label(led_on)
    ldr(r1, [r0, 4])        # dirección base de SIO
    mov(r2, 1)
    lsl(r2, r2, 25)         # 1 << 25 para GPIO25
    str(r2, [r1, 0x14])     # GPIO output value set
    bx(lr)
   
    label(led_off)
    ldr(r1, [r0, 4])        # dirección base de SIO
    mov(r2, 1)
    lsl(r2, r2, 25)         # 1 << 25 para GPIO25
    str(r2, [r1, 0x18])     # GPIO output value clear
    bx(lr)
   
    label(START)
    bl(config_led)
    label(WHILE1)
    bl(led_on)
    bl(delay)                 # Espera un tiempo significativo
    bl(led_off)         # Apaga un LED
    bl(delay)                 # Espera un tiempo significativo
    b(WHILE1)
   
blink(registros)

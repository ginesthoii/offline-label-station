from machine import UART

uart = UART(2, baudrate=19200, tx=17, rx=16)

def p(data):
    if isinstance(data, str):
        uart.write(data.encode())
    else:
        uart.write(data)

def print_text(msg):
    p(msg + "\n\n")

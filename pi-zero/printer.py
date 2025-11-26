import serial
import adafruit_thermal_printer

uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000)
ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.69)
printer = ThermalPrinter(uart)

def printer_text(msg):
    printer.print(msg)
    printer.feed(2)

def printer_barcode(data):
    printer.print_barcode(data, printer.CODE128)
    printer.feed(2)

def printer_qr(text):
    from qrgen import render_qr
    img = render_qr(text)
    printer.print_bitmap(img.width, img.height, img.tobytes())
    printer.feed(3)

from printer import p

def print_barcode(data):
    p(b'\x1d\x6b\x49')
    p(bytes([len(data)]))
    p(data)
    p("\n\n")

import qrcode
import framebuf
from printer import p

def print_qr(text):
    qr = qrcode.QRCode(border=1)
    qr.add_data(text)
    qr.make()

    matrix = qr.get_matrix()
    size = len(matrix)
    scale = 4
    img_size = size * scale

    buf = bytearray(img_size * img_size)
    fb = framebuf.FrameBuffer(buf, img_size, img_size, framebuf.MONO_HLSB)

    for y in range(size):
        for x in range(size):
            color = 0 if matrix[y][x] else 1
            for dy in range(scale):
                for dx in range(scale):
                    fb.pixel(x*scale+dx, y*scale+dy, color)

    for row in range(img_size):
        p(b'\x1B\x2A\x00' + bytes([img_size]) + b'\x00')
        p(buf[row*img_size:(row+1)*img_size])
        p(b'\n')

    p("\n\n")

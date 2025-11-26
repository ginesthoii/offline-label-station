from PIL import Image
import qrcode

def render_qr(text):
    qr = qrcode.make(text)
    qr = qr.resize((200, 200))
    return qr.convert("1")

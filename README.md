
# offline-label-station

A fully offline, solar/battery-friendly label system for homesteads, workshops, barns, inventories, livestock, bins, gear, camping, personal use. 

## Prints:
- QR codes
- Barcodes (UPC / EAN / Code128)
- Custom text labels
- Inventory tags
- Livestock health records
- Storage bin labels

## Runs on:
- ESP32 (ultra low power)
- Raspberry Pi Zero 2 W (full kiosk + offline web UI)
- NFC tag → auto-print pipeline

Everything runs completely offline.

---

## Features

✔ ESP32 firmware for quick barcode/QR printing  
✔ Pi Zero label kiosk with terminal UI  
✔ Offline Flask web interface  
✔ JSON datastore for inventories & livestock  
✔ Printable thermal templates (384px width)  
✔ Livestock Health QR Schema  
✔ NFC → auto-print workflow  
✔ systemd autostart  

---

## Folder Structure
```
offline-label-station/
│
├── README.md
├── LICENSE
│
├── esp32/
│   ├── main.py
│   ├── menu.py
│   ├── printer.py
│   ├── barcode.py
│   ├── qr.py
│   └── templates.py
│
├── pi-zero/
│   ├── kiosk.py
│   ├── printer.py
│   ├── qrgen.py
│   ├── barcodes.py
│   ├── nfc_reader.py
│   ├── datastore.py
│   ├── web/
│   │   ├── app.py
│   │   ├── templates/
│   │   │   ├── index.html
│   │   │   ├── print_label.html
│   │   │   └── inventory.html
│   │   └── static/
│   │       ├── style.css
│   │       └── client.js
│   └── autostart.service
│
├── data/
│   ├── inventory.json
│   ├── animals.json
│   └── bins.json
│
└── templates/
    ├── inventory_template.png.b64
    ├── livestock_template.png.b64
    └── bin_template.png.b64
```

---

## Hardware Supported

- Adafruit Tiny Thermal Printer (#2751)
- Adafruit Mini Thermal Printer (#597)
- Any ESC/POS-compatible serial/USB thermal printer (384px width)
- ESP32-S3 / ESP32-WROOM
- Raspberry Pi Zero 2 W
- PN532 NFC board

---

## Quick Start — Pi Zero
```
sudo apt update
sudo apt install python3-pip python3-flask python3-pil libnfc-bin
pip3 install pyserial qrcode adafruit-circuitpython-thermal-printer
Run kiosk:
python3 pi-zero/kiosk.py
Enable autostart:
sudo cp pi-zero/autostart.service /etc/systemd/system/
sudo systemctl enable autostart
sudo systemctl start autostart
```

## Quick Start — ESP32 (MicroPython)
```
Copy esp32/ folder to device:
ampy put main.py
ampy put *.py
Reboot ESP32 → menu appears.
```

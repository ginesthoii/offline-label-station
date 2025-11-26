import os
from printer import printer_text, printer_barcode, printer_qr
from datastore import get_inventory_label, get_animal_label, get_bin_label
from nfc_reader import read_nfc

def menu():
    while True:
        os.system("clear")
        print("--- OFFLINE LABEL KIOSK ---")
        print("1) Print QR")
        print("2) Print Barcode")
        print("3) Custom Text")
        print("4) Inventory (from JSON)")
        print("5) Livestock (from JSON)")
        print("6) Bin (from JSON)")
        print("7) NFC Scan → Print")
        print("8) Exit")

        choice = input("Select: ")

        if choice == "1":
            printer_qr(input("QR text: "))
        elif choice == "2":
            printer_barcode(input("Barcode: "))
        elif choice == "3":
            printer_text(input("Text: "))
        elif choice == "4":
            printer_text(get_inventory_label())
        elif choice == "5":
            printer_text(get_animal_label())
        elif choice == "6":
            printer_text(get_bin_label())
        elif choice == "7":
            tag = read_nfc()
            printer_text(f"NFC TAG: {tag}")
            printer_qr(tag)
        else:
            break

menu()

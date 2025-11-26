from printer import print_text
from barcode import print_barcode
from qr import print_qr
from templates import inventory_label, livestock_label, bin_label

def menu():
    while True:
        print("\n--- OFFLINE LABEL STATION ---")
        print("1) Print QR Code")
        print("2) Print Barcode")
        print("3) Print Custom Text")
        print("4) Inventory Label (template)")
        print("5) Livestock Label (template)")
        print("6) Bin Label (template)")
        print("7) Exit")

        choice = input("Select: ")

        if choice == "1":
            print_qr(input("QR text: "))

        elif choice == "2":
            print_barcode(input("Barcode: "))

        elif choice == "3":
            print_text(input("Text: "))

        elif choice == "4":
            print_text(inventory_label())

        elif choice == "5":
            print_text(livestock_label())

        elif choice == "6":
            print_text(bin_label())

        else:
            break

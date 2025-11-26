from flask import Flask, render_template, request
from printer import printer_qr, printer_barcode, printer_text
from datastore import get_inventory_label, get_animal_label, get_bin_label

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/print", methods=["POST"])
def print_label():
    mode = request.form["mode"]
    data = request.form["data"]

    if mode == "qr":
        printer_qr(data)
    elif mode == "barcode":
        printer_barcode(data)
    elif mode == "text":
        printer_text(data)

    return render_template(
        "print_label.html",
        mode=mode,
        data=data
    )

@app.route("/inventory")
def inventory():
    return render_template("inventory.html", label=get_inventory_label())

app.run(host="0.0.0.0", port=5000)

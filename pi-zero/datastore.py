import json
from pathlib import Path

DATA_DIR = Path("data")

def load_json(name):
    return json.load(open(DATA_DIR / name))

def get_inventory_label():
    item = load_json("inventory.json")[0]
    return (
        f"ITEM: {item['name']}\n"
        f"ID: {item['id']}\n"
        f"Location: {item['location']}\n"
        f"Category: {item['category']}\n"
    )

def get_animal_label():
    a = load_json("animals.json")[0]
    return (
        f"Animal: {a['name']}\n"
        f"Species: {a['species']}\n"
        f"Tag: {a['tag']}\n"
        f"Birth: {a['birth']}\n"
    )

def get_bin_label():
    b = load_json("bins.json")[0]
    return (
        f"BIN: {b['bin_id']}\n"
        f"Contents: {b['contents']}\n"
        f"Updated: {b['updated']}\n"
    )

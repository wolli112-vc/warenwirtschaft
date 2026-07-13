#!/usr/bin/env python3
import json
import os
from datetime import datetime
from flask import Flask, render_template, request, jsonify

DATA_FILE = "/share/warenwirtschaft/inventory.json"
LEGACY_FILE = "/data/inventory.json"

print(f"[Warenwirtschaft] Data file path: {os.path.abspath(DATA_FILE)}")

def _ensure_dir(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

def _maybe_migrate():
    """Kopiere alte Daten aus /data nach /share, falls vorhanden."""
    if os.path.exists(LEGACY_FILE) and not os.path.exists(DATA_FILE):
        _ensure_dir(DATA_FILE)
        try:
            with open(LEGACY_FILE, "r", encoding="utf-8") as src:
                with open(DATA_FILE, "w", encoding="utf-8") as dst:
                    dst.write(src.read())
            print(f"[Warenwirtschaft] Daten von {LEGACY_FILE} nach {DATA_FILE} migriert.")
        except Exception as e:
            print(f"[Warenwirtschaft] Migration fehlgeschlagen: {e}")

def load_data():
    _maybe_migrate()
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return []

def save_data(data):
    _ensure_dir(DATA_FILE)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("[Warenwirtschaft] Daten gespeichert.")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/items", methods=["GET"])
def get_items():
    items = load_data()
    # Sortiere nach Kategorie, dann Verfallsdatum
    items.sort(key=lambda x: (x.get("category", "").lower(), x.get("expires", "9999-99-99")))
    return jsonify(items)

@app.route("/api/categories", methods=["GET"])
def get_categories():
    items = load_data()
    cats = sorted(set(i.get("category", "").strip() for i in items if i.get("category", "").strip()))
    return jsonify(cats)

@app.route("/api/items", methods=["POST"])
def add_item():
    data = request.get_json()
    items = load_data()
    new_item = {
        "id": datetime.now().strftime("%Y%m%d%H%M%S%f"),
        "quantity": int(data.get("quantity", 1)),
        "product": data.get("product", "").strip(),
        "category": data.get("category", "").strip(),
        "expires": data.get("expires", "").strip()
    }
    items.append(new_item)
    save_data(items)
    return jsonify(new_item), 201

@app.route("/api/items/<item_id>", methods=["PUT"])
def update_item(item_id):
    data = request.get_json()
    items = load_data()
    for item in items:
        if item["id"] == item_id:
            if "quantity" in data:
                item["quantity"] = max(0, int(data["quantity"]))
            if "product" in data:
                item["product"] = data["product"].strip()
            if "category" in data:
                item["category"] = data["category"].strip()
            if "expires" in data:
                item["expires"] = data["expires"].strip()
            save_data(items)
            return jsonify(item)
    return jsonify({"error": "Not found"}), 404

@app.route("/api/items/<item_id>", methods=["DELETE"])
def delete_item(item_id):
    items = load_data()
    items = [i for i in items if i["id"] != item_id]
    save_data(items)
    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8099)

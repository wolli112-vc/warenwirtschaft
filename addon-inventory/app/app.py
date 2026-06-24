#!/usr/bin/env python3
import json
import os
from datetime import datetime
from flask import Flask, render_template, request, jsonify

DATA_FILE = "/data/inventory.json"

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return []

def save_data(data):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/items", methods=["GET"])
def get_items():
    items = load_data()
    # Sortiere nach Verfallsdatum
    items.sort(key=lambda x: x.get("expires", "9999-99-99"))
    return jsonify(items)

@app.route("/api/items", methods=["POST"])
def add_item():
    data = request.get_json()
    items = load_data()
    new_item = {
        "id": datetime.now().strftime("%Y%m%d%H%M%S%f"),
        "quantity": int(data.get("quantity", 1)),
        "product": data.get("product", "").strip(),
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

#!/usr/bin/python3
"""
Flask app that displays product data from JSON or CSV using query parameters.
"""

from flask import Flask, request, render_template_string
import json
import csv

app = Flask(__name__)

PRODUCT_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
    <title>Products</title>
</head>
<body>
    <h1>Products</h1>

    {% if error %}
        <p>{{ error }}</p>
    {% elif products %}
        <table border="1" cellpadding="5" cellspacing="0">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Category</th>
                    <th>Price</th>
                </tr>
            </thead>
            <tbody>
                {% for product in products %}
                <tr>
                    <td>{{ product.name }}</td>
                    <td>{{ product.category }}</td>
                    <td>{{ product.price }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    {% else %}
        <p>No products available</p>
    {% endif %}
</body>
</html>
"""


def load_products_from_json(path="products.json"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        # Expect either a list or an object with a "products" key; we normalize to list
        if isinstance(data, list):
            products = data
        else:
            products = data.get("products", [])
    except (FileNotFoundError, json.JSONDecodeError):
        products = []
    return products


def load_products_from_csv(path="products.csv"):
    products = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": row.get("id"),
                    "name": row.get("name"),
                    "category": row.get("category"),
                    "price": row.get("price"),
                })
    except FileNotFoundError:
        products = []
    return products


@app.route("/products")
def products():
    source = request.args.get("source")
    id_param = request.args.get("id")

    if source not in ("json", "csv"):
        return render_template_string(PRODUCT_TEMPLATE, error="Wrong source", products=[])

    if source == "json":
        raw_products = load_products_from_json()
    else:
        raw_products = load_products_from_csv()

    # Normalize product keys so template can use product.name, etc.
    normalized = []
    for p in raw_products:
        normalized.append({
            "id": str(p.get("id")),
            "name": p.get("name"),
            "category": p.get("category"),
            "price": p.get("price"),
        })

    if id_param:
        filtered = [p for p in normalized if p["id"] == str(id_param)]
        if not filtered:
            return render_template_string(
                PRODUCT_TEMPLATE,
                error="Product not found",
                products=[]
            )
        products_to_display = filtered
    else:
        products_to_display = normalized

    return render_template_string(PRODUCT_TEMPLATE, error=None, products=products_to_display)


if __name__ == "__main__":
    app.run(port=5000)

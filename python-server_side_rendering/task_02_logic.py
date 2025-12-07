#!/usr/bin/python3
"""
Flask app that renders a dynamic items list using Jinja logic.
"""

from flask import Flask, render_template_string
import json

app = Flask(__name__)

ITEMS_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
    <title>Items List</title>
</head>
<body>
    <h1>Items List</h1>
    {% if items %}
    <ul>
        {% for item in items %}
        <li>{{ item }}</li>
        {% endfor %}
    </ul>
    {% else %}
    <p>No items found</p>
    {% endif %}
</body>
</html>
"""


@app.route("/items")
def items():
    try:
        with open("items.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            items_list = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []

    return render_template_string(ITEMS_TEMPLATE, items=items_list)


if __name__ == "__main__":
    app.run(port=5000)

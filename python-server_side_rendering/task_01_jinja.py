#!/usr/bin/python3
"""
Basic Flask app that renders simple pages using Jinja templates in strings.
"""

from flask import Flask, render_template_string

app = Flask(__name__)

INDEX_HTML = """<!doctype html>
<html lang="en">
<head>
    <title>My Flask App</title>
</head>
<body>
    <header>
        <h1>My Flask App</h1>
        <nav>
            <a href="/">Home</a> |
            <a href="/about">About</a> |
            <a href="/contact">Contact</a>
        </nav>
        <hr>
    </header>

    <h1>Welcome to My Flask App</h1>
    <p>This is a simple Flask application.</p>
    <ul>
        <li>Flask</li>
        <li>HTML</li>
        <li>Templates</li>
    </ul>

    <footer>
        <hr>
        <p>&copy; 2024 My Flask App</p>
    </footer>
</body>
</html>
"""

ABOUT_HTML = """<!doctype html>
<html lang="en">
<head>
    <title>My Flask App - About</title>
</head>
<body>
    <header>
        <h1>My Flask App</h1>
        <nav>
            <a href="/">Home</a> |
            <a href="/about">About</a> |
            <a href="/contact">Contact</a>
        </nav>
        <hr>
    </header>

    <h1>About Us</h1>
    <p>This page contains information about our simple Flask application.</p>

    <footer>
        <hr>
        <p>&copy; 2024 My Flask App</p>
    </footer>
</body>
</html>
"""

CONTACT_HTML = """<!doctype html>
<html lang="en">
<head>
    <title>My Flask App - Contact</title>
</head>
<body>
    <header>
        <h1>My Flask App</h1>
        <nav>
            <a href="/">Home</a> |
            <a href="/about">About</a> |
            <a href="/contact">Contact</a>
        </nav>
        <hr>
    </header>

    <h1>Contact Us</h1>
    <p>You can contact us at contact@myflaskapp.com.</p>

    <footer>
        <hr>
        <p>&copy; 2024 My Flask App</p>
    </footer>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(INDEX_HTML)


@app.route("/about")
def about():
    return render_template_string(ABOUT_HTML)


@app.route("/contact")
def contact():
    return render_template_string(CONTACT_HTML)


if __name__ == "__main__":
    app.run(port=5000)

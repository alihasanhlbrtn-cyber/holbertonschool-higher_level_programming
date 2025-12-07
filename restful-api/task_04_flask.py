#!/usr/bin/python3
"""
Simple REST-style API using Flask.

Endpoints:
    GET  /              -> "Welcome to the Flask API!"
    GET  /status        -> "OK"
    GET  /data          -> JSON list of all usernames
    GET  /users/<username>
                         -> JSON user object or 404 {"error": "User not found"}
    POST /add_user      -> Add user from JSON body
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users.
# Do NOT prefill with test data when pushing to checker.
# Structure:
# users = {
#   "alice": {
#       "username": "alice",
#       "name": "Alice",
#       "age": 25,
#       "city": "San Francisco"
#   },
#   ...
# }
users = {}


@app.route("/")
def home():
    """Root endpoint."""
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    """Status endpoint."""
    return "OK"


@app.route("/data")
def get_usernames():
    """
    Return a JSON list of all usernames stored in the API.
    Example: ["jane", "john"]
    """
    # Use sorted for deterministic order (helps testing),
    # but not strictly required by the spec.
    usernames = sorted(users.keys())
    return jsonify(usernames)


@app.route("/users/<username>")
def get_user(username):
    """
    Return the full user object for the given username.
    If user does not exist, return 404 with {"error": "User not found"}.
    """
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Add a new user from JSON body.

    Expected JSON format:
    {
        "username": "alice",
        "name": "Alice",
        "age": 25,
        "city": "San Francisco"
    }

    Error cases:
        - Invalid JSON           -> 400 {"error": "Invalid JSON"}
        - Missing username       -> 400 {"error": "Username is required"}
        - Username already exists-> 409 {"error": "Username already exists"}
    """
    data = request.get_json(silent=True)

    # Invalid or non-JSON body
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Make sure stored object includes the username field as well
    user_obj = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city"),
    }

    users[username] = user_obj

    return jsonify({
        "message": "User added",
        "user": user_obj
    }), 201


if __name__ == "__main__":
    # Run with:
    #   flask --app task_04_flask.py run
    # or simply:
    #   python3 task_04_flask.py
    app.run()

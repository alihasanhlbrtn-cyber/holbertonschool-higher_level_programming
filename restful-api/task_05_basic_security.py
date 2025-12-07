#!/usr/bin/python3
"""
API Security and Authentication with Flask

Features:
- Basic HTTP Authentication (Flask-HTTPAuth)
- JWT-based Authentication (Flask-JWT-Extended)
- Role-based access control for admin-only route
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
    get_jwt,
)

app = Flask(__name__)


app.config["JWT_SECRET_KEY"] = "super-secret-key-change-me"

jwt = JWTManager(app)
auth = HTTPBasicAuth()


users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}


 
@auth.verify_password
def verify_password(username, password):
    """Verify username/password for basic auth."""
    user = users.get(username)
    if not user:
        return None
    if not check_password_hash(user["password"], password):
        return None
 
    return user["username"]


@auth.error_handler
def basic_auth_error():
    """Return 401 for basic auth failures."""
    return jsonify({"error": "Unauthorized access"}), 401


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """Protected by HTTP Basic Auth."""
    return "Basic Auth: Access Granted"




@app.route("/login", methods=["POST"])
def login():
    """
    Authenticate user and return JWT token.

    Expected JSON body:
    {
        "username": "user1",
        "password": "password"
    }
    """
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):

        return jsonify({"error": "Invalid credentials"}), 401


    additional_claims = {"role": user["role"]}
    access_token = create_access_token(identity=username, additional_claims=additional_claims)

    return jsonify({"access_token": access_token}), 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """Protected by JWT."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """
    Route only accessible to admin users.

    Returns 403 with {"error": "Admin access required"} if non-admin.
    """
    claims = get_jwt()
    role = claims.get("role")

    if role != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"




@jwt.unauthorized_loader
def handle_unauthorized_error(err):

    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):

    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()

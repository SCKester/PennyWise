from flask import Blueprint, jsonify, request, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from datetime import datetime
import os

from db import db
from models.user import User

auth_bp = Blueprint("auth", __name__)

# --- rate limiter ---
limiter = Limiter(key_func=get_remote_address, default_limits=[])

# --- secret + signer ---
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-change-me")
token_signer = URLSafeTimedSerializer(SECRET_KEY)

# --- helper to verify token ---
def verify_token(token: str, max_age_seconds: int = 60 * 60 * 24):
    try:
        return token_signer.loads(token, max_age=max_age_seconds)
    except (BadSignature, SignatureExpired):
        return None


# --- register ---
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json(force=True) or {}
    email = (data.get("email") or "").strip().lower()
    password = data.get("password") or ""

    if not email or not password:
        return jsonify({"error": "email and password required"}), 400

    # check if user exists
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "email already registered"}), 409

    pw_hash = generate_password_hash(password)
    user = User(email=email, pw_hash=pw_hash)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "registered", "user": user.to_dict()}), 201


# --- login ---
@limiter.limit("5 per 5 minutes")
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json(force=True) or {}
    email = (data.get("email") or "").strip().lower()
    password = data.get("password") or ""

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.pw_hash, password):
        return jsonify({"success": False, "message": "invalid credentials"}), 401

    user.last_login = datetime.utcnow()
    db.session.commit()

    token = token_signer.dumps({"email": email, "uid": user.id})

    resp = make_response(jsonify({"success": True, "user": user.to_dict()}))
    arewe = "yea" if (os.getenv("FLASK_ENV") == "production") else "no"
    print("are we in production?" + arewe)
    resp.set_cookie(
        "session",
        token,
        httponly=True,
        secure=os.getenv("FLASK_ENV") == "production",
        samesite="Lax",
        max_age=60 * 60 * 24,
    )
    return resp, 200


# --- get current user ---
@auth_bp.route("/me", methods=["GET"])
def me():
    token = request.cookies.get("session")
    payload = verify_token(token) if token else None
    if not payload:
        return jsonify({"error": "unauthorized"}), 401

    user = User.query.filter_by(email=payload["email"]).first()
    if not user:
        return jsonify({"error": "unauthorized"}), 401

    return jsonify(user.to_dict()), 200


# --- logout ---
@auth_bp.route("/logout", methods=["POST"])
def logout():
    resp = make_response(jsonify({"success": True}))
    resp.delete_cookie("session")
    return resp, 200

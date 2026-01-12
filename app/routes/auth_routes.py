# app/routes/auth.py v3

from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from app.models.user import User
from main import db

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')

# Login route v3
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or 'email' not in data or 'password' not in data:
        return jsonify({"message": "Email and password required"}), 400

    user = User.query.filter_by(email=data['email']).first()
    if not user:
        return jsonify({"message": "User not found"}), 404

    if not check_password_hash(user.password_hash, data['password']):
        return jsonify({"message": "Incorrect password"}), 401

    # Optional interview purpose demo: return a dummy token or just a success message for now
    return jsonify({"message": f"Login successful! Welcome {user.username}"}), 200

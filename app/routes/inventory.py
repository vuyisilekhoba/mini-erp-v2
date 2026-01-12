# app/routes/inventory.py

from flask import Blueprint, jsonify
from app.utils.auth_decorators import token_required, admin_required

inventory_bp = Blueprint("inventory", __name__, url_prefix="/inventory")


@inventory_bp.route("/", methods=["GET"])
@token_required
def view_inventory(current_user):
    return jsonify({
        "message": "Inventory data",
        "accessed_by": current_user.username
    })


@inventory_bp.route("/admin", methods=["GET"])
@token_required
@admin_required
def admin_inventory(current_user):
    return jsonify({
        "message": "Admin inventory control panel",
        "admin": current_user.username
    })

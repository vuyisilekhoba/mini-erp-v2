from flask import Blueprint, jsonify

bp = Blueprint('inventory', __name__)

@bp.route('/ping', methods=['GET'])
def ping():
    return jsonify({
        "status": "success",
        "message": "Inventory routes working"
    })

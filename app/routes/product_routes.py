from flask import Blueprint, jsonify

bp = Blueprint('products', __name__)

@bp.route('/ping', methods=['GET'])
def ping():
    return jsonify({
        "status": "success",
        "message": "Product routes working"
    })

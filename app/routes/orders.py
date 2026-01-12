from flask import Blueprint, request, jsonify
from main import db
from app.models.order import Order
from app.models.product import Product

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/', methods=['POST'])
def create_order():
    data = request.json
    product = Product.query.get(data['product_id'])
    if not product:
        return jsonify({"error": "Product not found"}), 404
    if product.quantity < data['quantity']:
        return jsonify({"error": "Insufficient stock"}), 400

    product.quantity -= data['quantity']
    new_order = Order(product_id=product.id, quantity=data['quantity'])
    db.session.add(new_order)
    db.session.commit()
    return jsonify({"message": "Order created successfully"}), 201

@orders_bp.route('/', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    result = [{"id": o.id, "product_id": o.product_id, "quantity": o.quantity, "created_at": o.created_at} for o in orders]
    return jsonify(result)

from flask import Blueprint, request, jsonify
from main import db
from app.models.product import Product

products_bp = Blueprint('products', __name__)

@products_bp.route('/', methods=['POST'])
def add_product():
    data = request.json
    new_product = Product(
        name=data['name'],
        sku=data['sku'],
        price=data['price'],
        quantity=data.get('quantity', 0)
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Product added successfully"}), 201

@products_bp.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()
    result = [{"id": p.id, "name": p.name, "sku": p.sku, "price": p.price, "quantity": p.quantity} for p in products]
    return jsonify(result)

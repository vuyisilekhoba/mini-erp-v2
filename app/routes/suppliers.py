from flask import Blueprint, request, jsonify
from main import db
from app.models.supplier import Supplier

suppliers_bp = Blueprint('suppliers', __name__)

@suppliers_bp.route('/', methods=['POST'])
def add_supplier():
    data = request.json
    new_supplier = Supplier(
        name=data['name'],
        email=data.get('email'),
        phone=data.get('phone')
    )
    db.session.add(new_supplier)
    db.session.commit()
    return jsonify({"message": "Supplier added successfully"}), 201

@suppliers_bp.route('/', methods=['GET'])
def get_suppliers():
    suppliers = Supplier.query.all()
    result = [{"id": s.id, "name": s.name, "email": s.email, "phone": s.phone} for s in suppliers]
    return jsonify(result)

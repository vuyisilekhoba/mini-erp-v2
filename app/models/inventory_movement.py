from main import db
from datetime import datetime

class InventoryMovement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('inventory_location.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    movement_type = db.Column(db.String(10), nullable=False)  # IN / OUT
    reference = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

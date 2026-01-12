import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# -----------------------
# Initialize Flask app Stock2shop demo purpose only with Adam v3
# -----------------------
app = Flask(__name__)

# -----------------------
# Configure Database (absolute path for safety) Stock2shop demo purpose only with Adam v3
# -----------------------
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'instance', 'mini_erp.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'  # SQLite DB path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # avoid warnings

# -----------------------
# Initialize SQLAlchemy Stock2shop demo purpose only with Adam v3
# -----------------------
db = SQLAlchemy(app)

# -----------------------
# Import Models Stock2shop demo purpose only with Adam v3
# Ensure User model exists with id, username, email, password_hash, role fields
# -----------------------
from app.models.user import User

# -----------------------
# Import and register Blueprints Stock2shop demo purpose only with Adam v3
# Auth Blueprint handles user registration/login and token generation
# Inventory Blueprint handles protected routes and admin role checks
# -----------------------
from app.routes.auth import auth_bp
app.register_blueprint(auth_bp)

from app.routes.inventory import inventory_bp
app.register_blueprint(inventory_bp)

# -----------------------
# Create tables if missing Stock2shop demo purpose only with Adam v3
# This ensures database is ready at app startup
# -----------------------
with app.app_context():
    db.create_all()
    print(f"Database ready at: {app.config['SQLALCHEMY_DATABASE_URI']}")

# -----------------------
# Test route Stock2shop demo purpose only with Adam v3
# Simple endpoint to verify server is running
# -----------------------
@app.route('/')
def home():
    return "Mini ERP V2 is running! Stock2shop demo purpose only with Adam v3"

# -----------------------
# Run server Stock2shop demo purpose only with Adam v3
# Debug mode is enabled for development/testing
# -----------------------
if __name__ == '__main__':
    app.run(debug=True)

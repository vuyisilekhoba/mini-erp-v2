# test_admin.py
from main import app, db
from app.models.user import User

with app.app_context():
    # Query the admin user
    admin = User.query.filter_by(username="admin").first()
    
    if admin:
        print("✅ Admin user exists!")
        print(f"Username: {admin.username}")
        print(f"Email: {admin.email}")
        print(f"Role: {admin.role}")
    else:
        print("❌ Admin user not found.")

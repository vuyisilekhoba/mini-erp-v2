# setup_db.py
from app import create_app, db
from app.models.user import User

app = create_app()

with app.app_context():
    print("Creating tables if they don't exist...")
    db.create_all()

    # Check if admin already exists
    admin_email = 'admin@test.com'
    if not User.query.filter_by(email=admin_email).first():
        admin = User(
            username='admin',
            email=admin_email,
            role='admin'
        )
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()
        print("Admin user created successfully!")
    else:
        print("Admin user already exists.")

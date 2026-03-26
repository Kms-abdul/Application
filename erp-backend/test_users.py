import os
from app import create_app
from extensions import db
from models import User
from helpers import verify_user_password, hash_user_password

app = create_app()
with app.app_context():
    users = User.query.all()
    print("--- User List ---")
    for u in users:
        print(f"User: '{u.username}', Email: '{u.useremail}', Password: '{u.password}'")
    print("-----------------")

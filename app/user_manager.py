from app.models import User
from app import db

def add_user(username, password):
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()

def remove_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()

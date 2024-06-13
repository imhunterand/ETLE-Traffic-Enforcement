from app import db

def create_database():
    db.create_all()

def drop_database():
    db.drop_all()

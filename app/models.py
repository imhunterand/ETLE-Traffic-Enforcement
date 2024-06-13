from app import db

class Violation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String(50))
    violation_type = db.Column(db.String(50))
    location = db.Column(db.String(100))
    vehicle_type = db.Column(db.String(50))

    def to_dict(self):
        return {
            'id': self.id,
            'timestamp': self.timestamp,
            'violation_type': self.violation_type,
            'location': self.location,
            'vehicle_type': self.vehicle_type
        }

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

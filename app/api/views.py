from flask import jsonify, request
from app.models import Violation
from app.api import api

@api.route('/violations', methods=['GET'])
def get_violations():
    violations = Violation.query.all()
    return jsonify([violation.to_dict() for violation in violations])

@api.route('/violations', methods=['POST'])
def create_violation():
    data = request.get_json()
    violation = Violation(**data)
    db.session.add(violation)
    db.session.commit()
    return jsonify(violation.to_dict()), 201

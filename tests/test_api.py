import unittest
from app.api.views import api
from app import app, db
from flask_testing import TestCase

class TestAPI(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_violations(self):
        response = self.client.get('/api/violations')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

    def test_create_violation(self):
        data = {
            'timestamp': '2021-01-01 00:00:00',
            'violation_type': 'speeding',
            'location': 'Street 123',
            'vehicle_type': 'car'
        }
        response = self.client.post('/api/violations', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['violation_type'], 'speeding')

if __name__ == '__main__':
    unittest.main()

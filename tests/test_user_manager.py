import unittest
from app.user_manager import add_user, remove_user
from app.models import User
from app import db

class TestUserManager(unittest.TestCase):

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_user(self):
        add_user('testuser', 'testpassword')
        user = User.query.filter_by(username='testuser').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.username, 'testuser')

    def test_remove_user(self):
        add_user('testuser', 'testpassword')
        user = User.query.filter_by(username='testuser').first()
        remove_user(user.id)
        user = User.query.filter_by(username='testuser').first()
        self.assertIsNone(user)

if __name__ == '__main__':
    unittest.main()

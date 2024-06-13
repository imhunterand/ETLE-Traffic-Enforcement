import unittest
from app.database import create_database, drop_database
from app import db

class TestDatabase(unittest.TestCase):

    def test_create_and_drop_database(self):
        create_database()
        self.assertTrue(db.engine.table_names())
        drop_database()
        self.assertFalse(db.engine.table_names())

if __name__ == '__main__':
    unittest.main()

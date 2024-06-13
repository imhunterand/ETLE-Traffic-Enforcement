import unittest
from app.email_notification import send_notification

class TestEmailNotification(unittest.TestCase):

    def test_send_notification(self):
        send_notification('test@example.com', 'Test Subject', 'Test Body')
        # Check email manually to verify

if __name__ == '__main__':
    unittest.main()

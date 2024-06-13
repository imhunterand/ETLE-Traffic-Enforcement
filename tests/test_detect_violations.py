import unittest
from app.detect_violations import detect_violations

class TestDetectViolations(unittest.TestCase):

    def test_detect_violations(self):
        detect_violations('output.avi')

if __name__ == '__main__':
    unittest.main()

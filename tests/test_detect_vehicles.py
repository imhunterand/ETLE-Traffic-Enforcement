import unittest
from app.detect_vehicles import detect_vehicles

class TestDetectVehicles(unittest.TestCase):

    def test_detect_vehicles(self):
        detect_vehicles('output.avi')

if __name__ == '__main__':
    unittest.main()

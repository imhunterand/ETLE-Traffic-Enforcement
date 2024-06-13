import unittest
from app.report_generator import generate_report
import os

class TestReportGenerator(unittest.TestCase):

    def test_generate_report(self):
        violations = [{'id': 1, 'timestamp': '2021-01-01 00:00:00', 'violation_type': 'speeding', 'location': 'Street 123', 'vehicle_type': 'car'}]
        generate_report(violations, 'report.pdf')
        self.assertTrue(os.path.exists('report.pdf'))
        os.remove('report.pdf')

if __name__ == '__main__':
    unittest.main()

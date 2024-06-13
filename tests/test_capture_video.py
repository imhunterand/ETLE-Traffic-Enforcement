import unittest
import os
from app.capture_video import capture_video

class TestCaptureVideo(unittest.TestCase):

    def test_capture_video(self):
        capture_video(duration=5)
        self.assertTrue(os.path.exists('output.avi'))
        os.remove('output.avi')

if __name__ == '__main__':
    unittest.main()

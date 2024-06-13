import unittest
from app.camera_manager import add_camera, remove_camera, cameras

class TestCameraManager(unittest.TestCase):

    def test_add_camera(self):
        add_camera('http://example.com/cam1')
        self.assertEqual(len(cameras), 1)
        self.assertEqual(cameras[0]['url'], 'http://example.com/cam1')

    def test_remove_camera(self):
        add_camera('http://example.com/cam1')
        remove_camera(1)
        self.assertEqual(len(cameras), 0)

if __name__ == '__main__':
    unittest.main()

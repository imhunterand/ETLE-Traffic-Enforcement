cameras = []

def add_camera(url):
    camera_id = len(cameras) + 1
    cameras.append({'id': camera_id, 'url': url})

def remove_camera(camera_id):
    global cameras
    cameras = [camera for camera in cameras if camera['id'] != camera_id]

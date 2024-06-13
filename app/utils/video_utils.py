import cv2

def capture_video_from_camera(camera_url, duration, output_path):
    cap = cv2.VideoCapture(camera_url)
    if not cap.isOpened():
        print("Error: Could not open video capture.")
        return

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (640, 480))

    start_time = time.time()
    while int(time.time() - start_time) < duration:
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    out.release()

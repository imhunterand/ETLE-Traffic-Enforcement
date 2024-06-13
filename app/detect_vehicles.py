import cv2

def detect_vehicles(video_path):
    cap = cv2.VideoCapture(video_path)
    vehicle_cascade = cv2.CascadeClassifier('vehicle_cascade.xml')

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        vehicles = vehicle_cascade.detectMultiScale(gray, 1.1, 1)

        for (x, y, w, h) in vehicles:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow('Vehicle Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_vehicles('output.avi')

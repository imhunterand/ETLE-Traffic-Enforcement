import cv2
import numpy as np
from tensorflow.keras.models import load_model
from utils.image_utils import preprocess_frame

model = load_model('vehicle_type_model.h5')

def predict_vehicle_type(frame):
    processed_frame = preprocess_frame(frame)
    prediction = model.predict(processed_frame)
    return np.argmax(prediction, axis=1)

def detect_vehicle_type(video_path):
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        vehicle_type = predict_vehicle_type(frame)
        cv2.putText(frame, f'Vehicle Type: {vehicle_type}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        cv2.imshow('Vehicle Type Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_vehicle_type('output.avi')

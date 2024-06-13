import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model('violation_model.h5')

def preprocess_frame(frame):
    frame = cv2.resize(frame, (224, 224))
    frame = np.expand_dims(frame, axis=0)
    frame = frame / 255.0
    return frame

def detect_violations(video_path):
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        processed_frame = preprocess_frame(frame)
        prediction = model.predict(processed_frame)
        violation = np.argmax(prediction, axis=1)

        if violation == 1:  # assuming 1 indicates a violation
            cv2.putText(frame, 'Violation Detected', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

        cv2.imshow('Violation Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_violations('output.avi')

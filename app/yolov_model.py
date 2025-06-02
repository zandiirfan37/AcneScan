from ultralytics import YOLO
import os
import cv2

# Load model YOLO hanya sekali saat pertama kali
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'model', 'best.pt')
model = YOLO(MODEL_PATH)

def predict_image(image_path):
    try:
        results = model(image_path)
        preds = results[0].probs
        if preds is not None:
            class_id = preds.top1
            return model.names[class_id].lower()
        else:
            return "tidak terdeteksi"
    except Exception as e:
        print(f"[ERROR] Gagal prediksi: {e}")
        return "tidak terdeteksi"

def detect_face(image_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30, 30))
    return len(faces) > 0

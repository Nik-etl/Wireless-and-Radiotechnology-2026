import os
import cv2
from dotenv import load_dotenv
from ultralytics import YOLO

# Load variables from .env
load_dotenv()

# Build the STREAM_URL dynamically
IP_ADDRESS = os.getenv("IP_ADDRESS", "127.0.0.1")
PORT = os.getenv("FLASK_PORT", "5000")
STREAM_URL = f"http://{IP_ADDRESS}:{PORT}/video_feed"

model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture(STREAM_URL)

if not cap.isOpened():
    print("Error: Could not open stream.")
    exit()

print(f"Stream opened at {STREAM_URL}. Running YOLO detection...")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    results = model(frame)
    annotated_frame = results[0].plot()

    cv2.imshow("YOLO Home Monitoring", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
# Intelligent Home Monitoring System

## Overview
This repository contains the code for a real-time, AI-enabled IoT video system. One laptop acts as a camera node, streaming live video over the local network. A second laptop acts as the AI monitoring node, receiving the stream and running YOLO object detection on each frame in real time.

Pipeline: Camera Node -> Network Stream -> AI Processing Node -> Detection Output

## Team setup
* Camera Node (Laptop A)
* AI Node (Laptop B)

## Execution Details

### How the stream was started
We ran the Flask application (`app.py`) on Laptop A, which accessed the webcam and broadcasted a live MJPEG stream over port 5000.

### How YOLO was run
We ran the `yolo_stream.py` script on Laptop B. This script connected to Laptop A's stream URL using OpenCV, downloaded the YOLOv8n model, and processed the incoming frames frame-by-frame, drawing bounding boxes around recognized objects.
frames in real time.

## How to run this project

1. Make sure both laptops are on the same WiFi network.
2. Find the IP address of the camera laptop (Laptop A) using `ipconfig`.
3. Open `yolo_stream.py` on Laptop B and update the `STREAM_URL` to match Laptop A's IP address.

**On Laptop A (Camera Node):**
1. Install dependencies:
   ```cmd
   pip install opencv-python flask

2. Start the stream:


    python app.py

On Laptop B (AI Node):

3. Install dependencies:

    pip install opencv-python ultralytics
4. Start the YOLO detection:


    python yolo_stream.py
    (Press 'q' in the video window to stop the detection)
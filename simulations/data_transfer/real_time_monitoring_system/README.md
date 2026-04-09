# Real-Time Home Monitoring System

## Overview
This repository contains the code and setup for a basic real-time video streaming system. One laptop acts as a camera node, capturing live video and broadcasting it over the local network using Python, OpenCV, and Flask. A second laptop acts as the viewer, connecting to the stream via a web browser.

Pipeline: Camera -> Capture -> Encode -> Stream -> Viewer

## Team setup
* Camera / Sender (Laptop A)
* Viewer / Receiver (Laptop B)

## Stream results
Did the viewer successfully watch the live stream?
Yes, once the Flask server started, we opened the browser on Laptop B, entered the sender's IP address and port 5000, and could see the live webcam feed updating in real time.

## How to run this project

1. Make sure both laptops are on the same WiFi network.
2. Install the required Python packages on the camera laptop:
   ```cmd
   pip install opencv-python flask
3. Start the stream on the camera laptop:

    python app.py
4. Find the IP address of the camera laptop (use ipconfig in the command prompt).

    On the viewer laptop, open a web browser and go to:
    http://[SENDER_IP]:5000 (Replace [SENDER_IP] with the actual IP address).
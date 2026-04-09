**This directory consists of the three tasks for the 9.4.26 lab session**

### Task 1: Automated Large-Data Transfer
* Protocol Focus: TCP/IP Sockets
* Application: Demonstrates reliable data transfer. The edge device buffers data locally and uses a simple handshake protocol to ensure the server received the file before deleting the local copy. This simulates remote sensors operating in areas with unstable radio coverage, where data must not be lost if the network drops.

### Task 2: Real-Time Video Streaming
* Protocol Focus: HTTP / MJPEG Streaming
* Application: Demonstrates continuous data transmission over a wireless network. This setup shows how live monitoring systems (like security cameras or drone video feeds) utilize network bandwidth to stream packets continuously without relying on local storage.

### Task 3: Intelligent Edge Processing
* Protocol Focus: Networked Data Pipelines
* Application: Demonstrates how raw wireless data streams are ingested and processed by a secondary computing node. By running YOLO object detection on the incoming network stream, this simulates smart industrial cameras, autonomous warehouse monitoring, and edge AI systems.
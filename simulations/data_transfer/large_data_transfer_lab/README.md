# Automated Large-Data IoT Pipeline

## Overview
This repository contains the code and documentation for an automated IoT pipeline built for Windows. The system simulates an edge device: it continuously records video, buffers it locally, sends it over a network to a server, and only deletes the local copy after the server confirms it was successfully received.

Pipeline Flow: Record -> Save -> Send -> Confirm -> Delete

## Results

### Did the automated system work?
Yes, the system ran in a continuous automated loop. The sender recorded 10-second clips every 2 minutes and successfully transferred them to the receiver without manual input.

### Were videos deleted only after confirmation?
Yes, the sender script waits for an exact "OK" message from the receiver.

## Troubleshooting
* Problem: We couldn't stop the receiver.py script with Ctrl+C because it was stuck waiting for a connection.
  * Fix: Added a timeout to the server socket and put the loop inside a try/except block so it catches the keyboard interrupt.
* Problem: The sender tried to send a video while the recorder was still saving it, crashing the connection.
  * Fix: We made the recorder save files as .tmp first, and then rename them to .mp4 only when they are fully saved and ready to send.

## How to Run

1. Install the required packages:
   ```cmd
   pip install opencv-python python-dotenv

2. Start the receiver:


    python receiver.py
3. Start the edge device (open two separate terminals):

    python recorder.py
    python sender.py
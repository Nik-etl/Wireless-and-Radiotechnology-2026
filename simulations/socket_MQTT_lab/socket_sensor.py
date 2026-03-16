import socket
import random
import time
import os
from dotenv import load_dotenv
# ran on device one 
load_dotenv()

SERVER_IP = os.getenv("SENSOR_SERVER_IP", "")
PORT = int(os.getenv("SENSOR_SERVER_PORT", ""))
INTERVAL_SECONDS = float(os.getenv("SENSOR_SEND_INTERVAL_SECONDS", ""))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((SERVER_IP, PORT))

while True:

    temperature = round(random.uniform(20,35),2)

    message = f"{temperature}"

    client.send(message.encode())

    print("Sensor value sent:", temperature)

    time.sleep(INTERVAL_SECONDS)

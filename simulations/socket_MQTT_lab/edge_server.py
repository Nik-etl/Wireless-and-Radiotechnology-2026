import socket
import paho.mqtt.client as mqtt
import os
from dotenv import load_dotenv
#Ran on device two acting as edge device
load_dotenv()

# TCP server settings
HOST = os.getenv("TCP_HOST", "")   # IP
PORT = int(os.getenv("TCP_PORT", ""))

# MQTT settings
broker = os.getenv("MQTT_BROKER", "")
topic = os.getenv("MQTT_TOPIC", "")
mqtt_port = int(os.getenv("MQTT_PORT", ""))

# MQTT client
mqtt_client = mqtt.Client()
mqtt_client.connect(broker, mqtt_port, 60)
mqtt_client.loop_start()

# TCP server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Waiting for sensor connection...")

conn, addr = server.accept()
print("Connected:", addr)

while True:

    data = conn.recv(1024)

    if not data:
        break

    value = data.decode()
    print("Sensor data:", value)

    # publish to MQTT
    mqtt_client.publish(topic, value)
    print("Published to MQTT:", value)

conn.close()
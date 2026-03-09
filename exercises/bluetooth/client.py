import socket
import random
import time

client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
client.connect(("XX:XX:XX:XX:XX:XX", 4))

print("Connected to Bluetooth server")

try:
    while True:
        temperature = round(random.uniform(20.0, 30.0), 1)
        message = f"Temperature: {temperature} C"
        client.send(message.encode("utf-8"))
        print("Sent:", message)
        time.sleep(5)

except OSError:
    pass

client.close()
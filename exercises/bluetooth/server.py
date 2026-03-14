import socket
import os
from dotenv import load_dotenv

load_dotenv()

bt_device_address = os.getenv("BT_DEVICE_ADDRESS")
bt_channel = int(os.getenv("BT_CHANNEL"))

def run_server():
    server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    server.bind((bt_device_address, bt_channel))
    server.listen(1)

    print("Waiting for Bluetooth client connection...")

    client, addr = server.accept()
    print(f"Connected to: {addr}")

    while True:
        request = client.recv(1024)
        request = request.decode("utf-8") # convert bytes to string
        if request.lower() == "close":
            # send response to the client which acknowledges that the
            # connection should be closed and break out of the loop
            client.send("close".encode("utf-8"))
            break
        # print data received from the client
        print(f"Received: {request}")
    # close connection socket with the client
    client.close()
    print("Connection to client closed")
    # close server socket
    server.close()


run_server()
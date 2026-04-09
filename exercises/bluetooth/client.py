import socket
import time
import threading
import os
from dotenv import load_dotenv

load_dotenv()

bt_device_address = os.getenv("BT_DEVICE_ADDRESS")
bt_channel = int(os.getenv("BT_CHANNEL"))

running = True #controls threads

def get_cpu_temp(): #Gets temperature from linux kernel
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
                temp_raw = f.read()
        temp_c = float(temp_raw) / 1000.0
        return temp_c

def send_loop(client: socket.socket) -> None:
        global running
        while running:
                temperature = get_cpu_temp()
                message = f"CPU Temperature: {temperature} C"
                client.send(message.encode("utf-8"))
                print("Sent:", message)
                time.sleep(5)

def recv_loop(client: socket.socket) -> None:
        #recieves messages from server
        global running
        while running:
                try:
                        data = client.recv(1024)
                except OSError:
                        break
                if not data:
                        break
                response = data.decode("utf-8")
                print(f"received: {response}")

                if response.lower() == "close":
                        running = False
                        break

def run_client():
        global running
        client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        client.connect((bt_device_address, bt_channel))
        print("Connected to Bluetooth server")

        sender = threading.Thread(target=send_loop, args=(client,), daemon=True)
        receiver = threading.Thread(target=recv_loop, args=(client,), daemon=True)
        sender.start()
        receiver.start()

        #main thread waiting for user command
        try:
                while running:
                        cmd = input("type 'close' to stop: ").strip().lower()
                        if cmd == 'close':
                                try:
                                        client.send(b"close")
                                except OSError:
                                        pass
                                running = False
                                break
        finally:
                client.close()
                print("connection to server closed")
run_client()
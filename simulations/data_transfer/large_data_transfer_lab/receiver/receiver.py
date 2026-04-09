import os
import socket
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

HOST = os.getenv("IP_ADDRESS", "127.0.0.1")
PORT = int(os.getenv("SOCKET_PORT", 5001))

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SAVE_FOLDER = os.path.join(SCRIPT_DIR, "received_videos")

os.makedirs(SAVE_FOLDER, exist_ok=True)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
server.settimeout(1.0)

print(f"Receiver is waiting for files on {HOST}:{PORT}...")

try:
    while True:
        try:
            conn, addr = server.accept()
        except socket.timeout:
            continue
            
        print(f"Connected by {addr}")

        # Receive filename first
        filename = conn.recv(1024).decode().strip()
        conn.sendall(b"FILENAME_OK")

        save_path = os.path.join(SAVE_FOLDER, filename)

        with open(save_path, "wb") as f:
            while True:
                data = conn.recv(4096)
                if data == b"EOF":
                    break
                f.write(data)

        print(f"Received: {filename}")
        conn.sendall(b"OK")
        conn.close()

except KeyboardInterrupt:
    print("\nReceiver stopped by user.")
finally:
    server.close()
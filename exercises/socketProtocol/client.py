import socket
import random
import threading
import time

running = True  # shared flag to control background threads


def send_loop(client: socket.socket) -> None:
    """Send random temperature every 5 seconds while running is True."""
    global running
    while running:
        msg = f"Temperature: {round(random.uniform(20.0, 30.0), 1)} C"
        try:
            client.send(msg.encode("utf-8")[:1024])
            print(f"Sent: {msg}")
        except OSError:
            # socket likely closed
            break
        time.sleep(5)


def recv_loop(client: socket.socket) -> None:
    #Receive messages from server and stop on 'closed'
    global running
    while running:
        try:
            data = client.recv(1024)
        except OSError:
            break

        if not data:
            break

        response = data.decode("utf-8")
        print(f"Received: {response}")

        if response.lower() == "closed":
            running = False
            break


def run_client() -> None:
    global running

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # set these to match server device IP and port
    server_ip = "127.0.0.1"
    server_port = 8000

    client.connect((server_ip, server_port))
    print(f"Connected to server {server_ip}:{server_port}")

    # start background threads for sending temps and receiving responses
    sender = threading.Thread(target=send_loop, args=(client,), daemon=True)
    receiver = threading.Thread(target=recv_loop, args=(client,), daemon=True)
    sender.start()
    receiver.start()

    # main thread: wait for user command
    try:
        while running:
            cmd = input("Type 'close' to stop: ").strip().lower()
            if cmd == "close":
                try:
                    client.send(b"close")
                except OSError:
                    pass
                running = False
                break
    finally:
        client.close()
        print("Connection to server closed")


run_client()

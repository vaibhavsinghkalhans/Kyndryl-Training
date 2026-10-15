# Day16.py
# Socket Programming + Security Scripting (Single File)

import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

# Server Function
def server():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)

        print(f"Server listening on {HOST}:{PORT}")

        conn, addr = server_socket.accept()

        with conn:
            print("Connected by:", addr)

            data = conn.recv(1024)

            if data:
                message = data.decode().strip()

                # Security Practice 1: Input Validation
                if len(message) > 100:
                    conn.send(b"Input too long")
                else:
                    print("Received:", message)
                    conn.send(b"Message received safely")

        server_socket.close()

    except Exception as e:
        # Security Practice 2: Error Handling
        print("Error:", e)

# Client Function
def client():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))

        message = "Hello Server"
        client_socket.send(message.encode())

        response = client_socket.recv(1024)
        print("Server replied:", response.decode())

        client_socket.close()

    except Exception as e:
        print("Client Error:", e)

# Run Server and Client
server_thread = threading.Thread(target=server)
server_thread.start()

# Give server time to start
import time
time.sleep(1)

client()

server_thread.join()

print("Program completed successfully.")
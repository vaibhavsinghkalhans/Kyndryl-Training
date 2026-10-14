import socket
import threading
import time

HOST = socket.gethostname()
PORT = 5000

# Server
def server():
    server_socket = socket.socket()
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print("Server: Waiting for connection...")

    conn, addr = server_socket.accept()
    print("Server: Connected by", addr)

    data = conn.recv(1024).decode()
    print("Server received:", data)

    conn.send("Hello from Server".encode())

    conn.close()
    server_socket.close()

# Client
def client():
    time.sleep(1)  # Wait for server to start

    client_socket = socket.socket()
    client_socket.connect((HOST, PORT))

    client_socket.send("Hello Server".encode())

    data = client_socket.recv(1024).decode()
    print("Client received:", data)

    client_socket.close()

# Run both
server_thread = threading.Thread(target=server)
client_thread = threading.Thread(target=client)

server_thread.start()
client_thread.start()

server_thread.join()
client_thread.join()

print("Communication completed!")

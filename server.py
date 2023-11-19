import socket
import threading



server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("127.0.0.1", 12345)
server_socket.bind(server_address)

print("Server is listening on", server_address)
import socket

def send_request(username, operation, filename, data, server_address):
    request = f"{username}|{operation}|{filename}|{data}"

    # Send the request to the server
    client_socket.sendto(request.encode(), server_address)

    # Receive and print the server's response
    response, _ = client_socket.recvfrom(1024)
    print("Server response:", response.decode())

# Set up the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("127.0.0.1", 12345)

# Authentication: Each client has a username
username = input("Enter your username: ")
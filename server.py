# server.py
import socket
import threading

# Dictionary to store client privileges based on their usernames
client_privileges = {"user1": ["read", "write"], "user2": ["read"],"user3":["read"]}

def handle_client_request(data, address):
    try:
        username, operation, filename, content = data.decode().split("|")
    except ValueError:
        response = "Invalid request format"
        server_socket.sendto(response.encode(), address)
        return

    # Authenticate client and get the privilege
    privilege = authenticate_client(username)

    # Check if the client is authenticated
    if privilege:
        try:
            if operation == "read" and "read" in privilege:
                with open(filename, "r") as file:
                    response = file.read()
            elif operation == "write" and "write" in privilege:
                with open(filename, "a") as file:
                    file.write("\n" + content)
                response = "Write operation successful"
            else:
                response = "Invalid privilege for the specified operation"
        except FileNotFoundError:
            with open(filename, "w") as file:
                response = "File not found. Created a new file."
    else:
        response = "Invalid username"

    server_socket.sendto(response.encode(), address)


def authenticate_client(username):
    return client_privileges.get(username, [])

def client_handler():
    while True:
        data, address = server_socket.recvfrom(1024)
        client_thread = threading.Thread(target=handle_client_request, args=(data, address))
        client_thread.start()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("192.168.132.78", 12345)
server_socket.bind(server_address)

print("Server is listening on", server_address)

threading.Thread(target=client_handler).start()

import socket
import threading

client_privileges = {"Rinesa": "read"}

def authenticate_client(username):
    return username in client_privileges and client_privileges[username] == "write"
def handle_client_request(data, address):
    try:
        username, privilege, operation, filename, content = data.decode().split("|")
    except ValueError:
        response = "Invalid request format"
        server_socket.sendto(response.encode(), address)
        return

    if authenticate_client(username):
        try:
            if privilege == "read":
                with open(filename, "r") as file:
                    response = file.read()
            elif privilege == "write":
                with open(filename, "a") as file:
                    file.write("\n" + content)
                response = "Write operation successful"
            else:
                response = "Invalid privilege"
        except FileNotFoundError:
            with open(filename, "w") as file:
                response = "File not found. Created a new file."
    else:
        response = "Invalid username or privilege"

    server_socket.sendto(response.encode(), address)



def client_handler():
    while True:
        data, address = server_socket.recvfrom(1024)
        client_thread = threading.Thread(target=handle_client_request, args=(data, address))
        client_thread.start()



server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("127.0.0.1", 12345)
server_socket.bind(server_address)

print("Server is listening on", server_address)

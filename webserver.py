import socket
import os

def handle_request(client_socket, request):
    # Parse the HTTP request
    request_lines = request.split('\r\n')
    filename = request_lines[0].split()[1]

    # Check if the file exists
    if os.path.exists(filename):
        # Read the file
        with open(filename, 'rb') as f:
            content = f.read()
        
        # Send HTTP response
        response = 'HTTP/1.1 200 OK\r\n\r\n'.encode() + content
    else:
        # File not found, send 404 response
        response = 'HTTP/1.1 404 Not Found\r\n\r\nFile Not Found'.encode()

    client_socket.sendall(response)
    client_socket.close()

def main():
    # Define the host and port
    host = '127.0.0.1'
    port = 8000

    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on http://{host}:{port} ...")

    while True:
        # Wait for a connection
        client_socket, _ = server_socket.accept()

        # Receive the request
        request = client_socket.recv(1024).decode()

        # Handle the request
        handle_request(client_socket, request)

if __name__ == "__main__":
    main()

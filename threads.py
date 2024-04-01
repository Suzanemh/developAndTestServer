import socket
import threading
import os

def parse_request(request):
    # Split the request by lines and get the first line
    request_lines = request.split('\r\n')
    first_line = request_lines[0]

    # Extract the requested filename from the first line
    filename = first_line.split()[1]

    return filename

def serve_file(filename):
    # Check if the file exists
    if os.path.exists(filename):
        # Read the file contents
        with open(filename, 'rb') as file:
            content = file.read()
        
        # Construct HTTP response with status 200 OK and file content
        response = 'HTTP/1.1 200 OK\r\n\r\n'.encode() + content
    else:
        # File not found, construct 404 Not Found response
        response = 'HTTP/1.1 404 Not Found\r\n\r\nFile Not Found'.encode()

    return response

def handle_client(client_socket, address):
    # Receive request from client
    request = client_socket.recv(1024).decode()

    # Parse request to extract filename
    filename = parse_request(request)

    # Serve requested file
    response = serve_file(filename)

    # Send response to client
    client_socket.sendall(response)

    # Close connection
    client_socket.close()

def main():
    # Define host and port
    host = '127.0.0.1'
    port = 8000

    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind socket to address
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(5)
    print(f"Server listening on http://{host}:{port} ...")

    while True:
        # Accept incoming connection
        client_socket, address = server_socket.accept()

        # Create and start thread to handle client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()

if __name__ == "__main__":
    main()

import socket
import argparse

def http_get_request(server_ip, server_port, filename):
    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((server_ip, server_port))

        # Send HTTP GET request
        request = f"GET {filename} HTTP/1.1\r\nHost: {server_ip}\r\n\r\n"
        client_socket.sendall(request.encode())

        # Receive response from the server
        response = b""
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            response += data

        # Display server response
        print(response.decode())
    
    finally:
        # Close the socket
        client_socket.close()

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="Simple HTTP Client")
    parser.add_argument("-i", "--server_ip", help="Server IP address or hostname", required=True)
    parser.add_argument("-p", "--server_port", help="Server port", type=int, required=True)
    parser.add_argument("-f", "--filename", help="File path at the server", required=True)
    args = parser.parse_args()

    # Call the function to send HTTP GET request
    http_get_request(args.server_ip, args.server_port, args.filename)

if __name__ == "__main__":
    main()

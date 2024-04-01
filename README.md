# Task 1: Making a simple webserver

You will develop a web server that handles one HTTP request at a time. Your web server should accept and parse the HTTP request, get the requested file from the server’s file system, create an HTTP response message consisting of the requested file preceded by header lines, and then send the response directly to the client. If the requested file is not present on the server, the server should send an HTTP “404 Not Found” message back to the client. 

Put an HTML file (e.g., index.html) in the same directory that the server is in. Run the server program. Open a browser and provide the corresponding URL. For example: http://127.0.0.1:8000/index.html 'index.html' is the name of the file you placed in the server directory. Note also the use of the port number after the colon. You need to replace this port number with whatever port you have used in the server code. In the above example, we have used the port number 8000. The browser should then display the contents of index.html. If you omit ”:8000”, the browser will assume port 80 and you will get the web page from the server only if your server is listening at port 80. Then try to get a file that is not present on the server. You should get a “404 Not Found” message.

### How to run Task 1:

1. Save it in a file, webserver.py.
2. Put an HTML file (e.g., index.html) in the same directory.
3. Open a terminal or command prompt, navigate to the directory containing the Python file and HTML file.
4. Run the Python script by executing `python3 webserver.py`.
5. Open a web browser and go to http://127.0.0.1:8000/index.html. You should see the contents of index.html displayed in your browser.


# Task 2: Making a web client

Instead of using a browser, write your own HTTP client to test your server. Your client will connect to the server using a TCP connection, send an HTTP request to the server, and display the server response as an output. You can assume that the HTTP request sent is a GET method. The client should take command-line arguments specifying the server IP address or hostname, the port at which the server is listening, and the path at which the requested object is stored on the server1. The following is an input command format to run the client.

```bash
python3 client.py -i server_ip -p server_port -f filename


### How to run Task 2:
python3 client.py -i 127.0.0.1 -p 8000 -f index.html '''




# Task 3 : Making a multi-threaded web server

Currently, your web server handles only one HTTP request at a time. You should implement a multithreaded server that is capable of serving multiple requests simultaneously. Using threading, first create a main thread in which your modified server listens for clients at a fixed port. When it receives a TCP connection request from a client, it will set up the TCP connection through another port and services the client request in a separate thread.

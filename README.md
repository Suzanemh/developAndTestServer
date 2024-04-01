#Task 1. 
Task 1: Making a simple webserver
You will develop a web server that handles one HTTP request at a time. Your web server should accept and parse the HTTP request, get the requested file from the server’s file system, create and HTTP response message consisting of the requested file preceded by header lines, and then send the
response directly to the client. If the requested file is not present in the server, the server should send an HTTP “404 Not Found” message back to the client. 


Put an HTML file (e.g., index.html) in the same directory that the server is in. Run the server program. Open a browser and provide the corresponding URL. For example: http://127.0.0.1:8000/index.html
‘index.html’ is the name of the file you placed in the server directory. Note also the use of the port number after the colon. You need to replace this port number with whatever port you have used in
the server code. In the above example, we have used the port number 8000. The browser should then display the contents of index.html. If you omit ”:8000”, the browser will assume port 80 and you will
get the web page from the server only if your server is listening at port 80. Then try to get a file that is not present at the server. You should get a “404 Not Found” message.

#How to run task 1:

Save it in a file, webserver.py.
Put an HTML file (e.g., index.html) in the same directory.
Open a terminal or command prompt, navigate to the directory containing the Python file and HTML file.
Run the Python script by executing python3 webserver.py.
Open a web browser and go to http://127.0.0.1:8000/index.html. 
You should see the contents of index.html displayed in your browser.

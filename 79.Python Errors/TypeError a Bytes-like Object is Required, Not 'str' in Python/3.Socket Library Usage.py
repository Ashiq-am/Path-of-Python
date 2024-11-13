import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('example.com', 80))

request = "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n"
sock.send(request)

# importing the sockets module
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
target = input('What you want to scan?: ')

# getting the ip address using gethostbyname
# function
t_IP = socket.gethostbyname(target)
print("Starting scan on host: ", t_IP)


def port_scan(port):
	try:
		s.connect((t_IP, port))
		return True
	except:
		return False


port = int(input("Enter the port number to be scanned: "))

if port_scan(port):
	print('Port', port, 'is open')
else:
	print("port", port, "is closed")

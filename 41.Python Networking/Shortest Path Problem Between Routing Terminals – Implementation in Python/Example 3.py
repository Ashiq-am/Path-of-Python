""


"""

# Code for Router 2
import socket
import sys
import pickle

for i in range(1) :

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((socket.gethostname(), 8896))
	sock.listen(1)
	connection, client_address = sock.accept()
	route =[]
	sockets =[8895, 8896, 8897, 8898]

	while 1:
		try:
			route = pickle.loads(connection.recv(1024))
	except EOFError:
		break	
		finally:
			break
	print("Traversed 2")

	socknext = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	if(len(route)>0):

	x = route[0]
		route.remove(x)
		dataroute = pickle.dumps(route)
		socknext.connect((socket.gethostname(), sockets[x]))
		try:
			socknext.send(dataroute) # try sendall
			data = socknext.recv(16)
			print(data)
	finally:
			print("")
		socknext.close()


"""
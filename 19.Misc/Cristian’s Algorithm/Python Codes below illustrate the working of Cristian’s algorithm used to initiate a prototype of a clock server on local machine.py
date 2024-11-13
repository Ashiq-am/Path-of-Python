# Python3 program imitating a clock server

import socket
import datetime


# function used to initiate the Clock Server
def initiateClockServer():
    s = socket.socket()
    print("Socket successfully created")

    # Server port
    port = 8000

    s.bind(('', port))

    # Start listening to requests
    s.listen(5)
    print("Socket is listening...")

    # Clock Server Running forever
    while True:
        connection, address = s.accept()          # Establish connection with client
        print('Server connected to', address)
        connection.send(str(datetime.datetime.now()).encode())   # Respond the client with server clock time
        connection.close()                            # Close the connection with the client process


# Driver function
if __name__ == '__main__':
    # Trigger the Clock Server
    initiateClockServer()

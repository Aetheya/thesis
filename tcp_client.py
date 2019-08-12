import socket
from time import sleep
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.1.10', 8888)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
        print('Running')
        while True:
                # Send data
                message = 'This is the message.  It will be repeated.'
                #print('sending "%s"' % message)
                sock.sendall(message)

                # Look for the response
                amount_received = 0
                amount_expected = len(message)

                while amount_received < amount_expected:
                        data = sock.recv(16)
                        amount_received += len(data)
                        #print('received "%s"' % data)
                sleep(0.01)

finally:
        print('closing socket')
        sock.close()
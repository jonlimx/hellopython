# A simple socket server
# See https://docs.python.org/3/library/socket.html for more details about Socket.

import socket
host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

print('Server is running on port %d; Press Ctrl-C to terminate.' % port)
while 1:
    clientsock, clientaddr = s.accept()
    clientfile = clientsock.makefile('rw')
    clientfile.write("Welcome, " + str(clientaddr) + "\n")
    clientfile.write("Please enter a string: ")
    line = clientfile.readline().strip()
    clientfile.write("You entered %d characters. \n" % len(line))
    clientfile.close()
    clientsock.close()


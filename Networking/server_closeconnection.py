# Four steps to set up a socket on server side.
# Step 1: Create the socket object.
# Step 2: Set the socket options.
# Step 3: Bind to a port and interface.
# Step 4: Listen for connections.


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 52533))
s.listen(1)
print "--------Waiting for connection--------"

while 1:
    conn, address = s.accept()
    print "Get connection from: ", conn.getpeername()
    conn.close()


# How to handle socket errors.
# How to execute: python socketerrors.py www.baidu.com http /
# Four kinds of socket errors as follows
# 1. socket.error - I/O and communication issues related.
# 2. socket.gaierror - address resolution issues.
# 3. socket.herror - like h_error in C
# 4. socket.timeout - socket timeout


import socket
import sys

host = sys.argv[1]
print host
textport = sys.argv[2]
print textport
filename = sys.argv[3]
print filename

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, e:
    print "Strange error creating socket: %s" % e
    sys.exit(1)

# Try parsing it as a numeric port number.
try:
    port = int(textport)
except ValueError:
    # That didn't work, so it's probably a protocol name.
    # Look it up instead.
    try:
        port = socket.getservbyname(textport, 'tcp')
    except socket.error, e:
        print "Couldn't find your port: %s" % e
        sys.exit(1)

try:
    s.connect((host, port))
except socket.gaierror, e:
    print "Address-related error connecting to server: %s" % e
    sys.exit(1)
except socket.error, e:
    print "Connection error: %s" % e
    sys.exit(1)

try:
    s.sendall("GET %s HTTP/1.0\r\n\r\n" % filename)
except socket.error, e:
    print "Error sending data: %s" % e
    sys.exit(1)

while 1:
    try:
        buf = s.recv(2048)
    except socket.error, e:
        print "Error receiving data: %s" % e
        sys.exit(1)
    if not len(buf):
        break
    sys.stdout.write(buf)

# How to use socket, how to get information from socket.
import socket


print("Creating socket...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Done.")

print("Looking up port number...")
port = socket.getservbyname('http', 'tcp')
print("Done.")

print("Connecting to remote host on port %d" % port)
s.connect(('www.baidu.com', port))
print("Done.")

soureAdd = s.getsockname()
destAdd = s.getpeername()

print("Connected from ({0} , {1})".format(soureAdd[0], soureAdd[1]))
print("Connected from ({0} , {1})".format(destAdd[0], destAdd[1]))


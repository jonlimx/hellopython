from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFIZE = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

try:
    while True:
        print('Waiting for message...')
        data, addr = udpSerSock.recvfrom(BUFIZE)
        udpSerSock.sendto(b'[%s] %s' % (bytes(ctime(), 'utf-8'), data), addr)
except socket.error:
    udpSerSock.close()

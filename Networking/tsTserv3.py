from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

try:
    while True:
        print('Waiting for connection...')
        tcpCliSock, addr = tcpSerSock.accept()
        print('...connected from:', addr)

        while True:
            data = tcpCliSock.recv(BUFIZE)
            if not data:
                break
            tcpCliSock.send(b'[%s] %s' % (bytes(ctime(), 'utf-8'), data))
        tcpCliSock.close()
except socket.error:
    tcpSerSock.close()

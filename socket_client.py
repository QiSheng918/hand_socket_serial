import socket

HOST = '192.168.1.168' # or 'localhost'
HOST = 'localhost'
PORT = 2333
BUFSIZ =1024
ADDR = (HOST,PORT)

tcpCliSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpCliSock.connect(ADDR)
data1 = tcpCliSock.recv(BUFSIZ)
print(data1)
while True:
     data1 = raw_input('>')
     data1 = str(data1)
     if not data1:
         break
     tcpCliSock.send(data1.encode())
     data1 = tcpCliSock.recv(BUFSIZ)
     if not data1:
         break
     print(data1)
tcpCliSock.close()

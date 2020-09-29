import socket
import time
import serial

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('0.0.0.0',2333))
s.listen(5)
ser=serial.Serial('/dev/ttyACM0',9600)

while True:
    print "waiting for connetion"   
    sock,addr=s.accept()
#    print ser.isOpen()
    if ser.isOpen():
        sock.send(b'serial opened,welcome')
    else:
        sock.send(b'serial closed,hand will not work')
        
    while True:
        data=sock.recv(1024)
#        print data 
        if not data:
            sock.send(b'send failed')
        else:
            sock.send(data.decode('utf-8'))
        ser.write(data)
    sock.close()
s.close()


#! /usr/bin/env python
# file: tsTclnt.py -- TCP timestamp client
# date: 2012-09-06 author: kyon

from socket import *

HOST = '192.168.0.115'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    
    data = raw_input('>')
    if not data:
        break
    tcpCliSock.send('%s\r\n' % data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print data.strip()

tcpCliSock.close()

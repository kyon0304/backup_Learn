#! /usr/bin/env python
# file: tsUclnt.py -- UDP timestamp client
# date: 2012-09-06 author: kyon

from socket import *

HOST = '192.168.0.115'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input('>')
    if not data:
        break
    udpCliSock.sendto(data, ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print data

udpCliSock.close()

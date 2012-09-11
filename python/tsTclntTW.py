#! /usr/bin/env python
# file: tsTclntTW.py -- Twisted Reactor TCP timestamp client
# date: 2012-09-06 author: kyon

from twisted.internet import protocol, reactor

HOST = '192.168.0.115'
PORT = 21567

class TSClntProtocol(protocol.Protocol):
    def sendData(self):
        data = raw_input('>')
        if data:
            print '...sending %s...' % data
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendData()

    def dataReceived(self, data):
        print data
        self.sendData()

class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntProtocol
    clientConnectionLost = clientConnectionFailed = \
    lambda self, connector, reason: reactor.stop()

reactor.connectTCP(HOST, PORT, TSClntFactory())
reactor.run()

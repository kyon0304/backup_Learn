#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# file: 17_4.py 循环链接
# date: 2012-10-12 author: kyon

def GetData():
    import urllib
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='
    num = '12345'
    cookies = []
    f = open('17-4.txt','w')
    while True:
        sp = urllib.urlopen(url+num)
        content = sp.read()
        num = content.split()[-1]
        cookie = sp.info()['Set-Cookie'].split(';')[0].split('=')[1]
        if cookie != 'deleted':
            cookies.append(cookie)
            print content
        else:
            break
    
    string = ''.join(cookies)
    print string
    f.write(string)
    f.close()

def DeCom():
    f = open('17-4.txt')
    string = f.read()
    f.close()
#    head = string.split('%')[0]
#    data = string.split('%')[1:]
#    data = [chr(int(d[0:2], 16))+d[2:] for d in data]
#    data = head+''.join(data)
#    print len(data)
    import urllib
    data = urllib.unquote_plus(string)

    import bz2
    dc = bz2.decompress(data)
    return dc

def Call():
    import xmlrpclib as XR
    server = XR.ServerProxy('http://huge:file@www.pythonchallenge.com/pc/phonebook.php')
    return server.phone('Leopold')

if __name__ == '__main__':
    print 'Hint:',DeCom()
    print 'answer is:', Call()

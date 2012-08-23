#! /usr/bin/env python
# file: rochambeau.py
# date: 2012-8-23

roch = {('p','r'):'You win',('r','s'):'You win!',('s','p'):'You win!',
        ('r','p'):'You lose',('s','r'):'You lose',('p','s'):'You lose'}

def wol():
    import random
    pr = '''
Enter your choice:
(P)aper/(R)ock/(S)cissors
'''
    user = raw_input(pr).split()[0].lower()
    com = random.choice('psr')
    print 'You choose [', user,'].computer choose [', com,']'
    if user == com:
        print 'draw'
    elif (user,com) not in roch.keys():
        print 'Invalid input!'
    else:
        print roch[(user,com)]

if __name__ == '__main__':
    try:
        wol()
    except (IOError,EOFError,KeyboardInterrupt,IndexError):
        print 'wrong input!'

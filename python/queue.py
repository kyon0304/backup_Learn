#! /usr/bin/env python
# file: queue.py
# date: 2012-8-22

queue = []

def enQ():
    queue.append(raw_input('Enter your string:').strip())

def deQ():
    if len(queue) == 0:
        print 'Cannot pop from an empty queue!'
    else:
        print 'Removed [', queue.pop(0), ']'

def viewQ():
    print queue

CMDs = {'e':enQ, 'd':deQ, 'v': viewQ}

def showmenu():
    pr = '''
(E)nqueue
(D)equeue
(V)iew
(Q)uit
Enter choice: '''

    while True:
        while True:
            try:
                choice = raw_input(pr).split()[0].lower()
            except (IOError,KeyboardInterrupt,IndexError):
                choice = 'q'
            print '\nYou picked: [%s]' % choice
            if choice not in 'edvq':
                print 'Invalid option, try again'
            else:
                break
        if choice == 'q':
            break
        CMDs[choice]()

if __name__ == '__main__':
    showmenu()

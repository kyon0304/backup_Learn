#! /usr/bin/env/ python

def init():
    with open('dou.txt') as infile:
        secrets = infile.read()
    secret = secrets.split(',')
    secrets = [int(i) for i in secret]
    pattern = range(ord('a'), ord('z')+1) + range(ord('A'), ord('Z')+1)+[ord("'"), ord(','), ord('.'), ord('-'), ord(' '), ord('?'), ord('('), ord(')'), ord('*'), ord('+'), ord('"'), ord('{'), ord('}'), ord('!'), ord(';'), ord(':'), ord('@'), ord ('%'), ord('~'), ord('['), ord(']'), ord('&'), ord('>'), ord('<')]+range(ord('0'), ord('9')+1)
    return secrets, pattern

def findKey(secrets, pattern):
    keys = []
    for num in range(0, 3):
        for i in range(ord('a'), ord('z')+1):
            for j in secrets[num::3]:
                if i^j not in pattern:
                    #print i^j,
                    break 
            else:
                print chr(i)
                keys.append(i)
    return keys
            
def getArticle(secrets, keys):
    count = 0
    article = []
    for i in secrets:
        article.append(chr(i^keys[count%3]))
        count += 1
    article = ''.join(article)
    print article
    
if __name__ == '__main__':
    secrets, pattern = init()
    keys = findKey(secrets, pattern)
    getArticle(secrets, keys)

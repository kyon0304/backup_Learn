#! /usr/bin/env python
# file: cleanFilenoMap.py
# date: 2012-09-13 author: kyon

def main():
    f = open("test")
    lines = [line.strip() for line in f if line.strip() != '']
    for line in lines:
        print line
    f.close()

main()

#! /usr/bin/env python
# file: cleanFile.py -- ex_chapter11-11
# date: 2012-09-13 author: kyon

def judge(line):
    while line[0] == ' ' or line[0] == '\n' or line[0] == '\t':
        line.pop(0)
        if len(line) == 0:
            break
    if len(line) > 0:
        line.pop(-1)
        while line[-1] == ' ':
            line.pop(-1)
        line.append('\n')
    return line

def main(name):
    f = open(name, 'r')
    nf = open('neat'+name, 'w')
    lines = []
    for eachline in f:
        lines.append(list(eachline))
    for items in map(judge, lines):
        for item in items:
            nf.write(item)
    f.close()
    nf.close()

main('test')

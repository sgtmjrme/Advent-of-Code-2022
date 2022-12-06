#!/usr/bin/env python3

file = 'day6input.txt'

def p1_search(line:str,buffersize:int):
    waits = 0
    buffersize -= 1
    for i,c in enumerate(line):
        hit = line.rfind(c,max(i-buffersize,0),i)
        if hit != -1:
            waits = max(hit - (i-buffersize) + 1,waits)
        if i > buffersize and waits == 0:
            return i + 1
        if waits > 0: waits -= 1

if __name__ == '__main__':
    line = ''
    with open(file,'r') as f: 
        line = f.readline()
    p1 = p1_search(line,4)
    p2 = p1_search(line,14)

    print(f'P1: {p1} - P2: {p2}')
    
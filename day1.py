#!/usr/bin/env python3
if __name__ == '__main__':
    with open('day1input.txt','r') as f: 
        sizes = [sum([int(y) for y in x.split('\n') if y != '']) for x in f.read().split('\n\n')]
        sizes.sort()
        print(f'P1:{sizes[-1]}-P2:{sizes[-3]+sizes[-2]+sizes[-1]}')

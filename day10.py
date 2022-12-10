#!/usr/bin/env python3

file = 'day10input.txt'

p1_results = []
p2_results = []

def print_p2():
    for i in range(len(p2_results)):
        if i%40 == 0: print()
        print(p2_results[i],end='')

def check_cycles(cycles,x):
    #P1
    if (cycles + 20) % 40 == 0:
        p1_results.append(cycles*x)
    pos = (cycles-1) % 40
    if (x-1 == pos) or (x == pos) or (x+1 == pos):
        p2_results.append('#')
    else: p2_results.append('.')

if __name__ == '__main__':
    x = 1
    cycles=0
    with open(file,'r') as f:
        while (line := f.readline()):
            splits = line.split(' ')
            cycles += 1
            check_cycles(cycles,x)
            if splits[0] == 'addx':
                cycles += 1
                check_cycles(cycles,x)
                x += int(splits[1])
    print(f'P1: {sum(p1_results)}')
    print_p2()
#!/usr/bin/env python3

from io import TextIOWrapper
import pdb

ans_arr = []
all_sizes = []

i = 0
output = {}

file = 'day7input.txt'

def rec(f:TextIOWrapper,d:dict):
    d['size'] = 0
    while line := f.readline()[:-1]:
        if line.startswith('$'):
            #Command
            if line == '$ ls':
                while line := f.readline()[:-1]:
                    if line.startswith('$'): break
                    if line.startswith('dir'):
                        d[line.split(' ')[1]] = {}
                    else:
                        d['size'] += int(line.split(' ')[0])
                if line == '': return d['size']
            if line == '$ cd ..':
                if d['size'] < 100000: ans_arr.append(d['size'])
                all_sizes.append(d['size'])
                return d['size']
            elif line.startswith('$ cd'): 
                dir_name = line.split(' ')[2]
                if 'size' in d[dir_name]: pass
                else: d['size'] += rec(f,d[dir_name])
    if line == '': return d['size']

def loop(f:TextIOWrapper):
    #WIP, not done with this yet
    filesystem = {}
    ans_arr = []
    f.readline() #Dump cd /
    for line in f:
        if line.startswith('$ ls'):
            pass

def get_p2(d: dict):
    total_space = 70000000
    necessary = 30000000
    current = d['size']
    need_delete = current + necessary - total_space
    all_sizes.sort()
    for i in all_sizes:
        if i > need_delete: return i

if __name__ == '__main__':
    
    with open(file,'r') as f:
        f.readline() #Throw away the first line
        rec(f,output)
    p2 = get_p2(output)
    print(output)
    print(f'P1: {sum(ans_arr)} - P2: {p2}')
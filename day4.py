#!/usr/bin/env python3
import re
data_input = 'day4input.txt'
def parse_p1(arr: 'list[int]'):
    if arr[0] <= arr[2] and arr[1] >= arr[3]: return 1
    elif arr[0] >= arr[2] and arr[1] <= arr[3]: return 1
    return 0

def parse_p2(arr: 'list[int]'):
    if arr[0] > arr[3] or arr[2] > arr[1]:
        return 0
    return 1

if __name__ == '__main__':
    p1 = 0
    p2 = 0
    p1_regex = r'[-,]'
    with open(data_input,'r') as f:
        for line in f:
            s = [int(x) for x in re.split(p1_regex,line.strip())]
            if len(s) < 4: continue
            p1 += parse_p1(s)
            p2 += parse_p2(s)
    print(f'P1:{p1}-P2:{p2}')
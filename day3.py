#!/usr/bin/env python3
#input_file = 'day3test.txt'
input_file = 'day3input.txt'

def get_points(char: str) -> int:
    val = ord(char[0])
    if val > 96: return val - 96 #Lowercase
    return val-38 #Uppercase

def p1_find_match(line: str) -> str:
    middle = len(line)//2 #Need integer division to ignore newline character
    second = line[middle:]
    for i in line[0:middle]:
        if i in second: 
            return i 

def p2_find_match(lines: 'list[str]') -> str:
    for i in lines[0]:
        if i in lines[1] and i in lines[2]:
            return i

if __name__ == '__main__':
    with open(input_file,'r') as f:
        p1 = 0
        p2 = 0
        p2_lines = []
        for line in f:
            p1 += get_points(p1_find_match(line))
            p2_lines.append(line)
            if len(p2_lines) > 2:
                p2 += get_points(p2_find_match(p2_lines))
                p2_lines.clear()

        print(f'P1:{p1}-P2:{p2}')
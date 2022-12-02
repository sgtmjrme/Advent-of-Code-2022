#!/usr/bin/env python3


if __name__ == '__main__':
    sizes: list[int] = []
    cur = 0
    with open('day1input.txt','r') as f:
        for line in f:
            line = line.strip()
            if line == '':
                sizes.append(cur)
                cur = 0
            else:
                cur += int(line.strip())
    sizes.sort()
    print(sizes)
    print(sizes[-3]+sizes[-2]+sizes[-1])
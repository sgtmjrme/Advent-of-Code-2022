#!/usr/bin/env python3

file = 'day9test2.txt'

def get_min_max(t: 'list[list[int]]'):
    xmin = 99999999
    xmax = -99999999
    ymin = 99999999
    ymax = -99999999
    for i in t:
        xmin = min(int(i[0]),xmin)
        xmax = max(int(i[0]),xmax)
        ymin = min(int(i[1]),ymin)
        ymax = max(int(i[1]),ymax)
    return xmin,xmax,ymin,ymax

def print_table(path: dict,tails: list,head: list):
    full = [head.copy()]
    full.extend(tails)
    for p in path:
        splits = p.split(',')
        full.append(splits)
    xmin,xmax,ymin,ymax = get_min_max(full)
    for y in range(ymax,ymin-1,-1):
        for x in range(xmin,xmax+1):
            c = 'x' if f'{x},{y}' in path else '.'
            for i,t in enumerate(tails):
                if t == [x,y]: c = i+1
            if head == [x,y]: c = 'H'
            print(str(c),end='')
        print()

def get_tail(head,tail,pos):
    avg = (head[pos]+tail[pos])/2
    return head[pos] if int(avg) != avg else int(avg)

def move(head,tail):
    if max(abs(head[0]-tail[0]),abs(head[1]-tail[1])) > 1:
        tail[0] = get_tail(head,tail,0)
        tail[1] = get_tail(head,tail,1)
        return f'{tail[0]},{tail[1]}'
    return '0,0' #Just dump a value that's guaranteed to be there

if __name__ == '__main__':
    tail_0_path = {'0,0':1}
    tail_9_path = {'0,0':1}
    head = [0,0]
    tails = [[0,0] for _ in range(9)]
    with open(file,'r') as f:
        while (line := f.readline().strip()):
            splits = line.split(' ')
            for _ in range(int(splits[1])):
                if splits[0] == 'U': head[1] += 1
                if splits[0] == 'D': head[1] -= 1
                if splits[0] == 'L': head[0] -= 1
                if splits[0] == 'R': head[0] += 1
                tail_point = move(head,tails[0])
                tail_0_path[tail_point] = tail_0_path[tail_point] + 1 if tail_point in tail_0_path else 1
                for i in range(1,len(tails)):
                    tail_point = move(tails[i-1],tails[i])
                    if i == 8: tail_9_path[tail_point] = tail_9_path[tail_point] + 1 if tail_point in tail_9_path else 1
    print(len(tail_0_path))
    print(len(tail_9_path))
    print_table(tail_9_path,tails,head)

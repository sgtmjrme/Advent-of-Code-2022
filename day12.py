#!/usr/bin/env python3

from collections import deque
from dataclasses import dataclass
import pdb
from queue import Queue

file = 'day12input.txt'

@dataclass
class pnt:
    pos: tuple[int,int]
    val: int
    prev: tuple[int,int]

    def __add__(self,other):
        return (self.pos[0]+other[0],self.pos[1]+other[1])

def build_maze(maze: list[list[int]],start: tuple[int,int], end: tuple[int,int], maze_x: int, maze_y: int):
    queue: Queue[pnt] = Queue()
    seen = set()
    seen.add(start)
    queue.put(pnt(start,0,None))
    lowest_max = 99999999999
    while not queue.empty():
        next_val = queue.get()
        next_weight = next_val.val + 1
        for dir in [(1,0),(0,1),(0,-1),(-1,0)]:
            new_square = next_val + dir
            if new_square in seen: continue
            if new_square[0] < 0 or new_square[1] < 0 or new_square[0] >= maze_x or new_square[1] >= maze_y: continue
            if maze[new_square[1]][new_square[0]] - maze[next_val.pos[1]][next_val.pos[0]] > 1:
                continue
            if new_square == end:
                lowest_max = min(lowest_max,next_weight)
                continue
            seen.add(new_square)
            queue.put(pnt(new_square,next_weight,tuple([i * -1 for i in dir])))

    return lowest_max

if __name__ == '__main__':
    map = []
    with open(file,'r') as f:
        map.extend([[ord(c)-96 for c in line] for line in f.read().split('\n')])
    
    starts = deque()
    #Find start and end
    start=None
    end=None
    for j,l in enumerate(map):
        for i,c in enumerate(map[j]):
            if c == -13: starts.appendleft((i,j));map[j][i]=1
            elif c == -27: end = (i,j);map[j][i]=27
            elif c == 1: starts.append((i,j))
    
    #Do the maze!
    size = len(map)*len(map[0])
    initial = True
    lowest_weight = 99999999
    for start in starts:
        weight = build_maze(map,start,end,len(map[0]),len(map))
        if initial: print(f'P1: {start} {weight}');initial = False
        lowest_weight = min(lowest_weight,weight)
    print(f'P2: {lowest_weight}')
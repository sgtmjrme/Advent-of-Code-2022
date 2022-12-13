#!/usr/bin/env python3

from dataclasses import dataclass
from queue import Queue

file = 'day12input.txt'

@dataclass
class pnt:
    pos: tuple[int,int]
    val: int
    prev: tuple[int,int]

    def __add__(self,other):
        return (self.pos[0]+other[0],self.pos[1]+other[1])

def build_maze(maze: list[list[int]],start: tuple[int,int], end: tuple[int,int], maze_x: int, maze_y: int) -> list[int]:
    queue: Queue[pnt] = Queue()
    seen = set()
    seen.add(end)
    queue.put(pnt(end,0,None))
    weights = set()
    while not queue.empty():
        next_val = queue.get()
        next_weight = next_val.val + 1
        for dir in [(1,0),(0,1),(0,-1),(-1,0)]:
            new_square = next_val + dir
            if new_square in seen: continue
            if new_square[0] < 0 or new_square[1] < 0 or new_square[0] >= maze_x or new_square[1] >= maze_y: continue
            if maze[next_val.pos[1]][next_val.pos[0]] - maze[new_square[1]][new_square[0]] > 1:
                continue
            if new_square == start:
                weights.add(next_weight)
                return next_weight, weights
            if maze[new_square[1]][new_square[0]] == 1:
                weights.add(next_weight)
                continue
            seen.add(new_square)
            queue.put(pnt(new_square,next_weight,tuple([i * -1 for i in dir])))

if __name__ == '__main__':
    map = []
    with open(file,'r') as f:
        map.extend([[ord(c)-96 for c in line] for line in f.read().split('\n')])
    
    #Find start and end
    start=None
    end=None
    for j,l in enumerate(map):
        for i,c in enumerate(map[j]):
            if c == -13: start = (i,j);map[j][i]=1
            elif c == -27: end = (i,j);map[j][i]=27
    
    #Do the maze!
    lastweight, weights = build_maze(map,start,end,len(map[0]),len(map))
    print(f'P1: {lastweight}')
    print(f'P2: {min(weights)}')
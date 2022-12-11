#!/usr/bin/env python3

from collections import deque
import pdb


class Monkey():
    monkey_num: int
    objects: deque[int]
    operation: str
    test_num: int
    test_options: list[bool]
    inspections = 0

    def __init__(self,s: str) -> None:
        splits = s.split('\n')
        self.test_options = [-1,-1]
        for line in splits:
            if line.startswith('Monkey'):
                self.monkey_num = line.split(' ')[1][:-1]
                continue
            line = line.strip()
            if line.startswith('Starting'):
                self.objects = deque([int(x) for x in line.split(':')[1].split(',')])
                continue
            if line.startswith('Operation'):
                self.operation = line.split('=')[1]
                continue
            space_split = line.split(' ')
            if line.startswith('Test'):
                self.test_num = int(space_split[3])
            elif line.startswith('If true'):
                self.test_options[True] = int(space_split[5])
            elif line.startswith('If false'):
                self.test_options[False] = int(space_split[5])
        assert(self.test_options[False] != -1 and self.test_options[True] != -1)

    def inspect(self, am: list):
            while len(self.objects) > 0:
                self.inspections+=1
                obj = self.objects.popleft()
                obj = int(eval(self.operation.replace('old',str(obj))))
                obj //= 3
                am[self.test_options[obj % self.test_num == 0]].objects.append(obj)

    def __str__(self):
        return f'Monkey {self.monkey_num}:{",".join([str(x) for x in self.objects])}'

    def __lt__(self, other):
        return self.inspections < other.inspections

    def __le__(self, other):
        return self.inspections <= other.inspections

    def __eq__(self, other):
        return self.inspections == other.inspections

    def __ne__(self, other):
        return self.inspections != other.inspections

    def __gt__(self, other):
        return self.inspections > other.inspections

    def __ge__(self, other):
        return self.inspections >= other.inspections


all_monkeys: list[Monkey] = []
file = 'day11input.txt'

rounds = 20

if __name__ == '__main__':
    with open(file,'r') as f:
        for s in f.read().split('\n\n'):
            all_monkeys.append(Monkey(s))
    for _ in range(rounds):
        for monkey in all_monkeys:
            monkey.inspect(all_monkeys)
    all_monkeys.sort()
    p1 = all_monkeys[-2].inspections * all_monkeys[-1].inspections
    print(f'P1: {p1}')
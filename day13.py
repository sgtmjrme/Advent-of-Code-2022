#!/usr/bin/env python3

from copy import deepcopy
import json
import pdb

file = 'day13input.txt'

def compare(p1in,p2in): #False = p1 > p2, True = p1 < p2, None = Equal
    p1 = deepcopy(p1in)
    p2 = deepcopy(p2in)
    if isinstance(p1,p2.__class__) and isinstance(p1,int):
        if p1 < p2: return True #Less than, good to go
        elif p1 > p2: return False #Greater than, bad case
        return None #Equal to
    for i in range(len(p1)):
        #print(f'Loop - {p1} - {p2}')
        if i >= len(p2): return False #P1 is longer, exit
        if isinstance(p1[i],p2[i].__class__): #If classes match
            if (ret := compare(p1[i],p2[i])) == None: continue
            return ret
        #One or the other is an int - convert to array
        if isinstance(p1[i],int) and isinstance(p2[i],list):
            p1[i] = [p1[i]]
        elif isinstance(p1[i],list) and isinstance(p2[i],int):
            p2[i] = [p2[i]]
        #It has to be two lists, compare them
        if (ret := compare(p1[i],p2[i])) != None: return ret
    #What if 0 length?
    if len(p1) == len(p2): return None
    return True

if __name__ == '__main__':
    with open(file,'r') as f:
        lines = f.read().split('\n\n')
    p1sum = 0
    all_inputs = []
    for i,pair in enumerate(lines):
        p1,p2 = [json.loads(x) for x in pair.split('\n')]
        all_inputs.append(p1)
        all_inputs.append(p2)
        ret = compare(p1,p2)
        assert(ret != None)
        if False:#not ret:
            print(pair)
            pdb.set_trace()
        p1sum += (ret * (i+1))
    print(f'P1: {p1sum}')

    all_inputs.extend([[[6]],[[2]]])
    #OH MY GOSH FOR PART 2 I NEED TO WRITE A FRICKING SORTING ALGORITHM
    for i in range(len(all_inputs)-1):
        for j in range(1,len(all_inputs) - i):
            if not compare(all_inputs[j-1],all_inputs[j]): all_inputs[j-1],all_inputs[j] = all_inputs[j],all_inputs[j-1]
    p2num = 1
    for i,val in enumerate(all_inputs):
        if val == [[2]] or val == [[6]]: p2num *= (i+1)
    print(f'P2: {p2num}')
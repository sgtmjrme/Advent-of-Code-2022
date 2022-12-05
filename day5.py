#!/usr/bin/env python3

import pdb
import re


data = 'day5input.txt'

regex = r'.(.)..?'

def search_output(val: str) -> 'list[str]':
    output = []
    matches = re.finditer(regex,val)
    for match in matches:
        output.append(match.group(1))
    return output

if __name__ == '__main__':
    with open(data,'r') as f:
        data_arr = []
        while (line := f.readline()) != '\n':
            if '[' in line: 
                results = search_output(line)
                if len(data_arr) == 0:
                    for i in range(0,len(results)): data_arr.append([])
                for i in range(0,len(results)):
                    if results[i] != ' ':
                        data_arr[i].append(results[i])
        for i in range(0,len(data_arr)):
            data_arr[i].reverse() #Make it a stack
        #Duplicate the table for P2
        p2_arr = []
        for i in range(0,len(data_arr)):
            p2_arr.append([])
            for j in data_arr[i]:
                p2_arr[i].append(j)
        while (line := f.readline()):
            splits = line.split(' ')
            i = 0
            fr = int(splits[3])-1
            to = int(splits[5])-1
            #p1
            while i < int(splits[1]):
                if len(data_arr[fr]) < 1: pdb.set_trace()
                data_arr[to].append(data_arr[fr].pop())
                i += 1
            #p2
            p2_arr[to].extend(p2_arr[fr][-i:])
            p2_arr[fr] = p2_arr[fr][0:-i]
        print(data_arr)
        print(f'P1:{"".join([x[-1] for x in data_arr])} - P2: {"".join([x[-1] for x in p2_arr])}')
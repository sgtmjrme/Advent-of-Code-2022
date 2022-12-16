#!/usr/bin/env python3

import re

file = 'day15input.txt'
check_line = 2000000

def dist(p1,p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def point_to_dict(pnt: tuple[int]):
    return f'{pnt[0]},{pnt[1]}'

def print_map(xmin,xmax,ymin,ymax,sensors,beacons):
    for sensor in sensors:
        for j in range(ymin,ymax+1):
            for i in range(xmin,xmax+1):
                val = '.'
                p = point_to_dict([i,j])
                if p in sensors: val = 'S'
                elif p in beacons: val = 'B'
                else:
                    check_point = [i,j]
                    p = point_to_dict(check_point)
                    if dist(sensors[sensor][0],check_point) <= sensors[sensor][1]:
                        val = '#'
                print(val,end='')
            print()

def range_intersect(r1,r2):
    if r1[0] > r2[1] or r2[0] > r1[1]:
        return False
    return True

def combine_ranges(ranges):
    combined_ranges = []
    for r in ranges:
        for cr in combined_ranges:
            if range_intersect(r,cr):
                cr[0] = min(r[0],cr[0])
                cr[1] = max(r[1],cr[1])
                combined_ranges = combine_ranges(combined_ranges)
                break
        else:
            combined_ranges.append(r)
    return combined_ranges


def size_row(check_line,sensors):
    #Get valid ranges along line
    ranges = []
    for sensor in sensors:
        s = sensors[sensor]
        if sensors[sensor][0][1] + sensors[sensor][1] < check_line or sensors[sensor][0][1] - sensors[sensor][1] > check_line: continue
        #The sensor will at least be on the line - generate a range
        length_along_range = s[1] - abs(s[0][1] - check_line)
        ranges.append([s[0][0]-length_along_range,s[0][0]+length_along_range])
    #Combine ranges
    combined_ranges = combine_ranges(ranges)
    #P2 - if there are 2 ranges, based on the problem description there MUST be 1 number between them. 
    if len(combined_ranges) > 1:  
        #Find out which range is second, and subtract 1 off its starting value to get the "missing" point
        if combined_ranges[0][0] > combined_ranges[1][0]:
            return None, combined_ranges[0][0] - 1
        return None, combined_ranges[1][0]-1
    
    #Calc for P1
    beaconless = 0
    for r in combined_ranges:
        beaconless += (r[1] - r[0])
    return beaconless, None

def calc_freq(x,y):
    return 4000000*x+y

if __name__ == '__main__':
    sensors = {} # Point -> (intarr, dist to beacon)
    beacons = {} # Point -> (intarr)
    with open(file,'r') as f:
        r = r'Sensor at x=(-?[0-9]*), y=(-?[0-9]*): closest beacon is at x=(-?[0-9]*), y=(-?[0-9]*)'
        for line in f:
            matches = re.search(r,line)
            b_arr = (int(matches[3]),int(matches[4]))
            s_arr = (int(matches[1]),int(matches[2]))
            b_point = point_to_dict(b_arr)
            s_point = point_to_dict(s_arr) 
            sensors[s_point] = (s_arr, dist(s_arr,b_arr))
            beacons[b_point] = b_arr
    #P1
    beaconless,dump = size_row(check_line,sensors)
    print(f'P1: {beaconless}')
    #P2
    for row in range(0,4000000):
        if row % 10000 == 0: print(row)
        ret, num = size_row(row,sensors)
        if num != None: 
            print(f'P2: {calc_freq(num,row)}')
            break
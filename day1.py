with open('day1input.txt','r') as f: 
 s = [sum([int(y) for y in x.split('\n') if y]) for x in f.read().split('\n\n')]
 s.sort()
 print(f'P1:{s[-1]}-P2:{s[-3]+s[-2]+s[-1]}')

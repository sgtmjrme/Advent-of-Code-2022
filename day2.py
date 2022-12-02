#!/usr/bin/env python3

if __name__ == '__main__':
    #Generate tables
    p1_results_table = {}
    pl_num = {'X':0,'Y':1,'Z':2}
    opp_num = {'A':0,'B':1,'C':2}
    win = {0:0,1:3,2:6}
    for opp in ['A','B','C']:
        for pl in ['X','Y','Z']:
            mod_val = (pl_num[pl] - opp_num[opp] + 1) % 3 
            p1_results_table[f'{opp} {pl}'] = pl_num[pl] + 1 + win[mod_val]
    p2_results_table = {}
    win_num = {'X':-1,'Y':0,'Z':1}
    for opp in ['A','B','C']:
        for win_val in ['X','Y','Z']:
            mod_val = (win_num[win_val] + opp_num[opp]) % 3
            p2_results_table[f'{opp} {win_val}'] = mod_val + 1 + win[pl_num[win_val]]
    #Actually compute points
    p1=0
    p2=0
    with open('input.txt','r') as f:
        for line in f:
            line = line.strip()
            p1 += p1_results_table[line]
            p2 += p2_results_table[line]
    print(f'P1:{p1}-P2:{p2}')

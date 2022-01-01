# https://adventofcode.com/2021/day/3

from collections import defaultdict
from copy import copy

def read_input():
    with open('./inputs/day3.txt', 'r') as file:
        seq = file.read().strip().split('\n')
        return seq

def solution1():
    seq = read_input()
    d = defaultdict(int)
    for i in seq:
        for idx, k in enumerate(i):
            d[idx] += int(k)
    c1, c2 = "", ""
    for i in range(12):
        if d[i] > len(seq) // 2:
            c1 += "1"
            c2 += "0"
        else:
            c1 += "0"
            c2 += "1"
    c1 = int(c1, 2)
    c2 = int(c2, 2)
    return c1 * c2


def solution2():
    seq = read_input()
    seq0 = seq.copy()
    pos = 0
    while len(seq0) != 1:
        seq0 = checker(seq0, pos, 0)
        pos += 1
    
    seq1 = seq.copy()
    pos = 0
    while len(seq1) != 1:
        seq1 = checker(seq1, pos, 1)
        pos += 1
    
    c1 = int(seq0.pop(), 2)
    c2 = int(seq1.pop(), 2)
    return c1 * c2



def checker(seq, pos, aim):
    d = {'0':set(), '1':set()}
    for item in seq:
        d[item[pos]].add(item)
    if len(d['0']) == len(d['1']):
        return d[str(aim)]
    if len(d['0']) > len(d['1']):
        if aim:
            return d['0']
        else:
            return d['1']
    if aim:
        return d['1']
    else:
        return d['0']

        
    

print(solution1())
print(solution2())


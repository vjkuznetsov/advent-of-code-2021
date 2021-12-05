# https://adventofcode.com/2021/day/1

def read_input():
    with open('./inputs/day1.txt', 'r') as file:
        seq = tuple(map(int, file.read().strip().split('\n')))
        return seq

def solution(k):
    seq, s = read_input(), 0
    for i in range(k, len(seq)):
        if seq[i] > seq[i-k]:
            s += 1
    return s

print(solution(k=1))
print(solution(k=3))
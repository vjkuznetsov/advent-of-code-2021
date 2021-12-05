# https://adventofcode.com/2021/day/1

def read_input():
    with open('./inputs/day1.txt', 'r') as file:
        seq = tuple(map(int, file.read().strip().split('\n')))
        return seq

def solution_part_one():
    seq, s = read_input(), 0
    for i in range(1, len(seq)):
        if seq[i] > seq[i-1]:
            s += 1
    return s

def solution_part_two():
    seq, s = read_input(), 0
    for i in range(3, len(seq)):
        if seq[i] > seq[i-3]:
            s += 1
    return s

print(solution_part_one())
print(solution_part_two())
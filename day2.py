# https://adventofcode.com/2021/day/2

def read_input():
    with open('./inputs/day2.txt', 'r') as file:
        seq = file.read().strip().split('\n')
        return seq

def solution1():
    seq = read_input()
    depth, position = 0, 0
    for cmd in seq:
        key, value = cmd.split(' ')
        value = int(value)
        if key == 'forward':
            position += value
        if key == 'up':
            depth -= value
        if key == 'down':
            depth += value
    return depth * position

def solution2():
    seq = read_input()
    aim, depth, position = 0, 0, 0
    for cmd in seq:
        key, value = cmd.split(' ')
        value = int(value)
        if key == 'forward':
            position += value
            depth += value * aim
        if key == 'up':
            aim -= value
        if key == 'down':
            aim += value
    return position * depth


print(solution1())
print(solution2())

from itertools import cycle
from math import lcm

with open("input.txt") as f:
    data = f.read().splitlines()

class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

node_dict = {}
for line in data[2:]:
    node_dict[line[0:3]] = Node(line[7:10], line[12:15])

instructions = cycle(data[0])

name = "AAA"
counter = 0
while name != "ZZZ":
    dir = next(instructions)
    if dir == "L":
        name = node_dict[name].left
    else:
        name = node_dict[name].right
    counter += 1

print(counter)

names = [name for name in node_dict.keys() if name[2] == "A"]
l = len(names)
all_z = False
max_z = 0
mults = [0] * l
for i, name in enumerate(names):
    instructions = cycle(data[0])
    counter = 0
    while name[2] != "Z":
        dir = next(instructions)
        if dir == "L":
            name = node_dict[name].left
        else:
            name = node_dict[name].right
        counter += 1
    mults[i] = counter

res = 1
for m in mults:
    res = lcm(res, m)

print(res)

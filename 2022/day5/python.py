import numpy as np

file1 = open("2022/day5/input1.txt", "r")
file2 = open("2022/day5/input2.txt", "r")
stacks = file1.readlines()
moves = file2.readlines()

def parse_line(str):
    str += " "
    l = len(str)
    out = []
    for i in range(0, int(np.round(l/4))):
        out.append(str[i*4+1].strip())
    return out

def move_one_box(stacks2, origin, target):
    stacks2[target] = stacks2[origin][0] + stacks2[target]
    stacks2[origin] = stacks2[origin][1:]
    return stacks2

def move_multiple_boxes(stacks3, origin, target, num):
    print("begin")
    print(stacks3)
    stacks3[target] = stacks3[origin][:num] + stacks3[target]
    stacks3[origin] = stacks3[origin][num:]
    print(origin, target, num)
    print(stacks3)
    return stacks3

stacks2 = [""] * 9
for line in stacks[:len(stacks)-1]:
    line = line[:len(line)-1]
    line = parse_line(line)
    for col in enumerate(line):
        stacks2[col[0]] += col[1]

stacks3 = stacks2.copy()
for line in moves:
    str = (line.strip()).split(" ")
    for i in range(0, int(str[1])):
        stacks2 = move_one_box(stacks2, int(str[3])-1, int(str[5])-1)
    stacks3 = move_multiple_boxes(stacks3, int(str[3])-1, int(str[5])-1, int(str[1]))

#print(stacks2)
print(stacks3)
print(''.join([stacks2[i][0] for i in range(9)]))
print(''.join([stacks3[i][0] for i in range(9)]))


import numpy as np
import copy

with open("input.txt") as f:
    data = f.read().splitlines()

for i, line in enumerate(data):
    try:
        s_pos = [line.index("S"), i]
    except:
        continue

dir_sets = {"up": {"|", "7", "F"}, "down": {"|", "L", "J"}, "left": {"-", "L", "F"}, "right": {"-", "7", "J"}}
dir_from_start = []
if data[s_pos[1]-1][s_pos[0]] in dir_sets["up"]:
    dir_from_start.append("down")
if data[s_pos[1]+1][s_pos[0]] in dir_sets["down"]:
    dir_from_start.append("up")
if data[s_pos[1]][s_pos[0]-1] in dir_sets["left"]:
    dir_from_start.append("right")
if data[s_pos[1]][s_pos[0]+1] in dir_sets["right"]:
    dir_from_start.append("left")

s_symb = dir_sets[dir_from_start[0]].intersection(dir_sets[dir_from_start[1]])
pos_list = [s_pos]

symb_dirs = {"|": ["up", "down"], "-": ["left", "right"], "L": ["up", "right"],
             "J": ["up", "left"], "7": ["left", "down"], "F": ["right", "down"],
             "S": ["stop"]}
from_to = {"up": "down", "down": "up", "left": "right", "right": "left"}

def move(pos, dir):
    match dir:
        case "up": return [pos[0], pos[1]-1]
        case "down": return [pos[0], pos[1]+1]
        case "left": return [pos[0]-1, pos[1]]
        case "right": return [pos[0]+1, pos[1]]
        case "stop": return pos
        case _ : print("REE")

dir = symb_dirs[list(s_symb)[0]][0]
pos_list.append(move(pos_list[-1], dir))

new = data[pos_list[-1][1]][pos_list[-1][0]]
dir = set(symb_dirs[new]) - {from_to[dir]}
while pos_list[-1] != s_pos:
    pos_list.append(move(pos_list[-1], list(dir)[0]))
    new = data[pos_list[-1][1]][pos_list[-1][0]]
    prev = data[pos_list[-2][1]][pos_list[-2][0]]
    dir = set(symb_dirs[new]) - {from_to[list(dir)[0]]}

l = (len(pos_list)-1) // 2
print(l)

noise = np.random.normal(0, 0.1, len(pos_list))
n_pos_list = copy.deepcopy(pos_list)
for p, _ in enumerate(n_pos_list):
    n_pos_list[p][0] += noise[p]
    n_pos_list[p][1] += noise[p]

eq = [] #ax+b [a,b]
for p, point in enumerate(n_pos_list[:-1]):
    x1, y1 = point[0], point[1]
    x2, y2 = n_pos_list[p+1][0], n_pos_list[p+1][1]
    a = (y1-y2)/(x1-x2)
    b = y1-a*x1
    eq.append([a, b])

def check_all_eq(p):
    n = 0
    for i, e in enumerate(eq):
        p1 = n_pos_list[i]
        p2 = n_pos_list[i+1]
        if p[1] > min(p1[1], p2[1]) and p[1] < max(p1[1], p2[1]):
            x = (p[1]-e[1])/e[0]
            if x > p[0]:
                n += 1
    return n

inside = []
for y, line in enumerate(data):
    print(y)
    for x, _ in enumerate(line):
        if [x, y] not in pos_list :
            if check_all_eq([x, y]) % 2 == 1:
                inside.append([x, y])

def return_unique(list_of_lists):
    return {x for x in set(tuple(x) for x in list_of_lists)}

area = set(return_unique(inside)) - set(return_unique(pos_list))
print(len(area))
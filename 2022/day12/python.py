import sys

sys.path.append('../../')

import graph

#load the file input.txt and split it into a list of lines
with open('test.txt') as f:
    data = f.read().splitlines()

#find the start and end points
for line in data:
    if 'S' in line:
        start = (line.index('S'), data.index(line))
        ind_S = data.index(line)
    if 'E' in line:
        goal = (line.index('E'), data.index(line))
        ind_E = data.index(line)

data[ind_S] = data[ind_S].replace('S', 'a')
data[ind_E] = data[ind_E].replace('E', 'z')

print(start, goal)
#variable storing alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_backwards = alphabet[::-1]

#get neighbors of a point if the index in alphabet is smaller than n+1
def neighbors(point):
    x, y = point
    cur_letter = data[y][x]
    l = []
    if y-1 >= 0 and alphabet.index(data[y-1][x]) <= alphabet.index(cur_letter) + 1:
        l.append((x, y-1))
    if y+1 < len(data) and alphabet.index(data[y+1][x]) <= alphabet.index(cur_letter) + 1:
        l.append((x, y+1))
    if x-1 >= 0 and alphabet.index(data[y][x-1]) <= alphabet.index(cur_letter) + 1:
        l.append((x-1, y))
    if x+1 < len(data[y]) and alphabet.index(data[y][x+1]) <= alphabet.index(cur_letter) + 1:
        l.append((x+1, y))
    return l

def neighbors_backwards(point):
    x, y = point
    cur_letter = data[y][x]
    l = []
    if y-1 >= 0 and alphabet_backwards.index(data[y-1][x]) <= alphabet_backwards.index(cur_letter) + 1:
        l.append((x, y-1))
    if y+1 < len(data) and alphabet_backwards.index(data[y+1][x]) <= alphabet_backwards.index(cur_letter) + 1:
        l.append((x, y+1))
    if x-1 >= 0 and alphabet_backwards.index(data[y][x-1]) <= alphabet_backwards.index(cur_letter) + 1:
        l.append((x-1, y))
    if x+1 < len(data[y]) and alphabet_backwards.index(data[y][x+1]) <= alphabet_backwards.index(cur_letter) + 1:
        l.append((x+1, y))
    return l

res = graph.a_star(start, goal, lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1]), neighbors)
print(len(res)-1)

# Part 2
res2 = []
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == 'b':
            res2.append(len(graph.a_star(goal, (x, y), lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1]), neighbors_backwards)))

print(min(res2))
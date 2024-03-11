import sys
sys.path.append('../../')

import utils
import numpy as np

def move_sand(cave, x, y):
    if y + 1 >= cave.shape[1] or x <= 0 or x + 1 >= cave.shape[0]:
        return [False, False]
    if cave[x, y+1] == 0:
        cave[x, y] = 0
        cave[x, y+1] = 2
        return move_sand(cave, x, y+1)
    else:
        if cave[x-1, y+1] == 0:
            cave[x, y] = 0
            cave[x-1, y+1] = 2
            return move_sand(cave, x-1, y+1)
        else:
            if cave[x+1, y+1] == 0:
                cave[x, y] = 0
                cave[x+1, y+1] = 2
                return move_sand(cave, x+1, y+1)
            else:
                return [False, True]

def drop_sand(cave, x, y):
    sand_not_still = True
    while sand_not_still:
        if cave[x, y] == 2:
            return False
        cave[x, y] = 2
        sand_not_still, sand_not_in_void = move_sand(cave, x, y)
    return sand_not_in_void

part2 = False
data = utils.load_to_list('input.txt')

min_x, max_x = 1000, 0
min_y, max_y = 0, 0
for line in data:
    coords = line.split('-> ')
    for c in coords:
        x, y = c.split(',')
        if int(x) < min_x:
            min_x = int(x)
        if int(x) > max_x:
            max_x = int(x)
        if int(y) < min_y:
            min_y = int(y)
        if int(y) > max_y:
            max_y = int(y)

x_off = min_x
if part2:
    max_y += 2
    if max_x - min_x + 1 < max_y * 2:
        min_x -= max_y
        max_x += max_y
    x_off = 300

cave = np.zeros((max_x - min_x + 1, max_y - min_y + 1), dtype=int)
for line in data:
    coords = line.split('-> ')
    for i_c, c in enumerate(coords[:-1]):
        x1, y1 = c.split(',')
        x2, y2 = coords[i_c + 1].split(',')
        if int(x1) == int(x2):
            for y in range(min(int(y1) - min_y, int(y2) - min_y), max(int(y1) - min_y, int(y2) - min_y) + 1):
                cave[int(x1) - x_off, y] = 1
        if int(y1) == int(y2):
            for x in range(min(int(x2) - x_off, int(x1) - x_off), max(int(x2) - x_off, int(x1) - x_off) + 1):
                cave[x, int(y1)] = 1

if part2:
    for x in range(cave.shape[0]):
        cave[x, cave.shape[1]-1] = 1

sand_not_in_void = True
n_sand = 0

while sand_not_in_void:
    n_sand += 1
    sand_not_in_void = drop_sand(cave, 500 - x_off, 0)

#for i in range(cave.shape[0]):
#    for j in range(cave.shape[1]):
#        print(cave[i, j], end='')
#    print()
print(n_sand-1)
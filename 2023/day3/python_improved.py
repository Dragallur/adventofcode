import numpy as np
import re

with open("input.txt") as f:
    data = f.read().splitlines()

def flatten(l):
    return [item for sublist in l for item in sublist]

def add_neighbors(r, c):
    neighbors = [[r-1, c-1], [r, c-1], [r+1, c-1],
                 [r-1, c], [r+1, c],
                 [r-1, c+1], [r, c+1], [r+1, c+1]]
    return [n for n in neighbors if n[0] >= 0 and n[1] >= 0 and n[0] < len(data) and n[1] < len(data)]

res = []
gears = {}
re_digit = re.compile("(\d+)")
for row, row_str in enumerate(data):
    for re_col in re_digit.finditer(row_str):
        ran = range(re_col.start(), re_col.end())
        digit_store = int(''.join([data[row][x] for x in ran]))
        neighbors = np.unique(flatten([add_neighbors(row, x) for x in ran]), axis=0)
        neighbors_vals = [data[x[0]][x[1]] for x in neighbors]

        if any([True for x in neighbors_vals if not x.isdigit() and x!="."]):
            res.append(digit_store)

        ind = [i for i, x in enumerate(neighbors_vals) if x == "*"]
        for i in ind:
            n = neighbors[int(i)]
            s = str(n[0])+","+str(n[1])
            if s in gears:
                gears[s][0] *= digit_store
                gears[s][1] += 1
            else:
                gears[s] = [digit_store, 1]

print(sum(res))

res2 = 0
for key in gears.keys():
    if gears[key][1] == 2:
        res2 += gears[key][0]

print(res2)
import numpy as np

with open("2023/day3/input.txt") as f:
    data = f.read().splitlines()

def add_neighbors(row, col, neighbors):
    for r in range(np.clip(row-1, 0, None), np.clip(row+2, None, len(data))):
        for c in range(np.clip(col-1, 0, None), np.clip(col+2, None, len(data[row]))):
            neighbors.append(str(r)+","+str(c))

res = []
gears = {}
for row, row_str in enumerate(data):
    iter_col = iter(enumerate(data[row]))
    for col, col_str in iter_col:
        digit_store = []
        neighbors = []
        while data[row][col].isdigit() == True:
            digit_store.append(data[row][col])
            add_neighbors(row, col, neighbors)
            col += 1
            if col >= len(data[row]):
                break
            next(iter_col)
        
        for n in set(neighbors):
            r, c = int(n.split(",")[0]), int(n.split(",")[1])
            part = False
            if not data[r][c].isdigit() and data[r][c]!=".":
                part = True
                if data[r][c] == "*":
                    if n in gears:
                        gears[n][0] *= int(''.join(digit_store))
                        gears[n][1] += 1
                    else:
                        gears[n] = [int(''.join(digit_store)), 1]
            if part:
                res.append(int(''.join(digit_store)))

print(sum(res))

res2 = 0
for key in gears.keys():
    if gears[key][1] == 2:
        res2 += gears[key][0]

print(res2)
import re
import copy

with open("input.txt") as f:
    data = f.read().splitlines()

expansion = 1_000_000
rows_expanded = []
for i, line in enumerate(copy.deepcopy(data)):
    if re.findall(r"(\#)", line) == []:
        rows_expanded.append(i)

n = 0
cols_expanded = []
data = list(map(list, zip(*data)))
data = [''.join(i) for i in data]
for i, line in enumerate(copy.deepcopy(data)):
    if re.findall(r"(\#)", str(line)) == []:
        #data.insert(i+n, empty)
        cols_expanded.append(i)
        n += 1

data = list(map(list, zip(*data)))
data = [''.join(i) for i in data]

def find_galaxies(data):
    galaxies = []
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char == "#":
                galaxies.append((i,j))
    return galaxies

galaxies = find_galaxies(data)

def distances(galaxies):
    distances = []
    for i, galaxy in enumerate(galaxies):
        for j, galaxy2 in enumerate(galaxies):
            if i != j:
                x_min, x_max = min(galaxy[0], galaxy2[0]), max(galaxy[0], galaxy2[0])
                y_min, y_max = min(galaxy[1], galaxy2[1]), max(galaxy[1], galaxy2[1])
                cols_to_expand = sum([1 for x in rows_expanded if x in range(x_min, x_max)])
                rows_to_expand = sum([1 for x in cols_expanded if x in range(y_min, y_max)])
                distances.append(abs(galaxy[0] - galaxy2[0]) + abs(galaxy[1] - galaxy2[1]) + (cols_to_expand + rows_to_expand)*expansion)
                if expansion > 1:
                    distances[-1] -=  cols_to_expand + rows_to_expand
    return distances

distances = distances(galaxies)
print(sum(distances)/2)
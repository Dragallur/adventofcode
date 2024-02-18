import sys
sys.path.append('../../')

import utils
import json
import functools

def search(l, r):
    out = None
    for i in range(min(len(l), len(r))):
        out = compare(l[i], r[i])
        if out != None:
            return out
    if len(l) < len(r):
        return 1
    if len(l) > len(r):
        return -1 

def compare(l, r):
    match (l, r):
        case (int(), int()):
            if l > r:
                return -1
            if l < r:    
                return 1
        case (list(), list()):
            return search(l, r)
        case (int(), list()):
            return compare([l], r)
        case (list(), int()):
            return compare(l, [r])

data = utils.load_to_list('input.txt')

ind = []
all_lines = [[[2]], [[6]]]

for i, line in enumerate(data[:-1]):
    if line != '' and data[i+1] != '':
        l = json.loads(data[i])
        r = json.loads(data[i+1])
        all_lines.extend([l, r])
    else:
        continue

    if compare(l, r) == 1:
        ind.append(i)

ind = [(i+4) // 3 for i in ind]
print("PART1:", sum(ind))

all_lines.sort(key=functools.cmp_to_key(compare), reverse=True)
res2 = (all_lines.index([[2]])+1) * (all_lines.index([[6]])+1)
print("PART2:", res2)


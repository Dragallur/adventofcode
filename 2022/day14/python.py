import sys
sys.path.append('../../')

import utils
import numpy as np

data = utils.load_to_list('test.txt')

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
cave = np.empty((max_x - min_x + 1, max_y - min_y + 1), dtype=int)

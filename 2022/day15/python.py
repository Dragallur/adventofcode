import sys
sys.path.append('../../')

import utils
import numpy as np
import re
from itertools import chain

def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

data = utils.load_to_list('input.txt')
#data = utils.load_to_list('test.txt')

sensors = []
beacons = []
distances = []
for line in data:
    line = line.split(":")
    r = re.compile(r'-?\d+')
    sensor = list(map(int, r.findall(line[0])))
    beacon = list(map(int, r.findall(line[1])))
    sensors.append(sensor)
    beacons.append(beacon)
    distances.append(dist(sensor, beacon))


min_x = min(min(sensors)[0], min(beacons)[0])
max_x = max(max(sensors)[0], max(beacons)[0])
d = max(list(map(dist, sensors, beacons)))

n = 0

last_sensor = None
#part 1
y = 2000000
for x in range(min_x-d, max_x+d+1):
    if [x, y] in sensors or [x, y] in beacons:
        continue
    if last_sensor is not None:
        if dist(sensors[last_sensor], (x, y)) <= distances[last_sensor]:
            n += 1
            continue
    for i, sensor in enumerate(sensors):
        if dist(sensor, (x, y)) <= distances[i]:
            last_sensor = i
            n += 1
            break

print(n)

#part 2
def generate_neighbors_fast(sensor, distance, xmin, xmax, ymin, ymax):
    distance += 1
    sensor = [sensor[0], sensor[1]]
    x_range = np.arange(sensor[0] - distance, sensor[0] + distance + 1)
    y_range = np.concatenate((np.arange(sensor[1], sensor[1] + distance), np.arange(sensor[1] + distance, sensor[1] - 1, -1)))
    y_range_neg = np.concatenate((np.arange(sensor[1], sensor[1] - distance, -1), np.arange(sensor[1] - distance, sensor[1] + 1)))

    neighbors = np.concatenate((np.vstack((x_range, y_range)).T, np.vstack((x_range, y_range_neg)).T))
    neighbors = np.unique(neighbors, axis=0)
    neighbors = neighbors[(neighbors[:, 0] >= xmin) & (neighbors[:, 0] <= xmax) & (neighbors[:, 1] >= ymin) & (neighbors[:, 1] <= ymax)]
    return neighbors

def dist_fast(p1, p2):
    return np.sum(np.abs(p1 - p2), axis=1)

def check_if_outside_fast(p1, p2, dist_p1):
    return dist_fast(p1, p2) > dist_p1

def diff2d(a, b):
    a = set(tuple(x) for x in a)
    b = set(tuple(x) for x in b)
    res = a.difference(b)
    res = np.array(list(res))
    return res

final_fast = []
for i, sensor in enumerate(sensors):
    neighbors_f = generate_neighbors_fast(sensor, distances[i], 0, 4000000, 0, 4000000)
    neighbors_f = np.unique(neighbors_f, axis=0)
    f_n = []
    for ii, ssensor in enumerate(sensors):
        ssensor_arr = np.full_like(neighbors_f, np.array([ssensor[0], ssensor[1]]))
        d_arr = np.full((neighbors_f.shape[0]), distances[ii])
        mask = np.logical_not(check_if_outside_fast(ssensor_arr, neighbors_f, d_arr))
        f_n.append(neighbors_f[mask])
    f_n = np.unique(np.concatenate(f_n), axis=0)
    if neighbors_f.shape[0] == f_n.shape[0]:
        diff = []
    else:
        f_n = f_n.tolist()
        neighbors_f = neighbors_f.tolist()
        diff = diff2d(neighbors_f, f_n)
    if len(diff) != 0:
        final_fast = diff
        break
print(final_fast, final_fast[0][0] * 4000000 + final_fast[0][1])
        



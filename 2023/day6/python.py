import numpy as np
from functools import reduce

with open("input.txt") as f:
    data = f.read().splitlines()

time = [int(x) for x in (data[0].split(":")[1]).split(" ") if x != ""]
distance = [int(x) for x in (data[1].split(":")[1]).split(" ") if x != ""]

def calc_dist_from_time(time_pressed, total_time):
    remaining_time = total_time - time_pressed
    dist = remaining_time * time_pressed
    return dist

res = []
for id, race in enumerate(range(len(time))):
    r = range(time[id])
    dist_travelled = list(map(calc_dist_from_time, r, [time[id]] * len(r)))
    res.append(sum([True for x in dist_travelled if x > distance[id]]))

print(reduce(lambda x, y: x*y, res))

#part2
time = ''.join([str(x) for x in time])
distance = ''.join([str(x) for x in distance])

def get_mid(low, high):
    return (int(high) + int(low)) // 2

race1 = [0, 0, False] #time pressed, distance travelled, T/F fast enough
race2 = [int(time)//2, calc_dist_from_time(int(time)//2, int(time)), True] 
race_temp = [0, 0, False]
while np.abs(int(race1[0]) - int(race2[0])) > 1:
    race_temp[0] = get_mid(race1[0], race2[0])
    race_temp[1] = calc_dist_from_time(int(race_temp[0]), int(time))
    race_temp[2] = int(race_temp[1]) > int(distance)
    if race_temp[2]:
        race2[:] = race_temp[:]
    else:
        race1[:] = race_temp[:]

print(int(time)-2*race2[0]+1)
import numpy as np

file = open("2022/day4/input.txt", "r")
data = file.readlines()

def create_range(string):
    low = int(string[:string.index("-")])
    high = int(string[string.index("-")+1:]) + 1
    return(np.arange(low, high))

total_intersections = 0
total_nonzero_intersections = 0
for line in data:
    line = line.strip()
    first = create_range(line[0:line.index(",")])
    second = create_range(line[line.index(",")+1:])
    intersection = np.intersect1d(first, second)
    if np.size(intersection) >= np.size(first) or np.size(intersection) >= np.size(second):
        total_intersections += 1
    
    if np.size(intersection) > 0:
        total_nonzero_intersections += 1

print(total_intersections)
print(total_nonzero_intersections)
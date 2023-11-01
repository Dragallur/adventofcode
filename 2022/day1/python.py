import numpy as np

file = open("2022/day1/input.txt", "r")
data = file.readlines()

each_elf = [0]
num_of_elves = 0

for line in data:
    if len(line.strip()) > 0:
        each_elf[num_of_elves] += int(line.strip())
    else:
        each_elf.append(0)
        num_of_elves += 1

each_elf = np.sort(each_elf)[::-1]
print(each_elf[0])
print(np.sum(each_elf[0:2]))
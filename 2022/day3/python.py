import numpy as np
import string as st

file = open("2022/day3/input.txt", "r")
data = file.readlines()

alphabet = st.ascii_lowercase + st.ascii_uppercase
total_priority = 0

for line in data:
    line = line.strip()
    length = len(line)
    rucksack1 = line[0:int(length/2)]
    rucksack2 = line[int(length/2):length]
    chars = list(set(rucksack1).intersection(rucksack2))
    total_priority += np.sum([alphabet.index(char)+1 for char in chars])

print(total_priority)

#part2
total_priority = 0

for line in enumerate(data):
    data[line[0]] = line[1].strip()

for i in range(0, len(data) // 3):
    elf1 = data[3*i]
    elf2 = data[3*i+1]
    elf3 = data[3*i+2]
    chars = list((set(elf1).intersection(elf2)).intersection(elf3))
    total_priority += np.sum([alphabet.index(char)+1 for char in chars])

print(total_priority)

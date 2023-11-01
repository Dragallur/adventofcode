import numpy as np

file = open("2022/day2/input.txt", "r")
data = file.readlines()

won = ["A Y", "B Z", "C X"]
tie = ["A X", "B Y", "C Z"]
your_turn = ["X", "Y", "Z"]
enemy_turn = ["A", "B", "C"]
score = 0

for line in data:
    line = line.strip()
    if line in won:
        score += 6
    elif line in tie:
        score += 3
    score += your_turn.index(line[2]) + 1
    
print(score)

#part 2
score = 0
for line in data:
    line = line.strip()
    if line[2] == "X":
        score += (enemy_turn.index(line[0]) + 2) % 3 + 1
    elif line[2] == "Y":
        score += 3 + enemy_turn.index(line[0]) + 1
    elif line[2] == "Z":
        score += 6 + (enemy_turn.index(line[0]) + 1) % 3 + 1

print(score)
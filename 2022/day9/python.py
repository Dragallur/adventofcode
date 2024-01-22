import numpy as np

with open("input.txt") as f:
    data = f.read().splitlines()

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def move(vec, object):
    object.x += vec.x
    object.y += vec.y

def vector_difference(head, tail): 
    return Node(head.x-tail.x, head.y-tail.y)

real_head = Node(0, 0)
n_tails = 9
tails = [Node(0, 0) for i in range(n_tails)]
vec = Node(0, 0)

visited_pos = [(tails[-1].x, tails[-1].y)]

for line in data:
    for i in range(int(line[2:])):
        vec.x = 0
        vec.y = 0
        if line[0] == "U":
            vec.y = 1
        if line[0] == "D":
            vec.y = -1
        if line[0] == "R":
            vec.x = 1
        if line[0] == "L":
            vec.x = -1
        move(vec, real_head)

        for tail, head in zip(tails, [real_head]+tails[:-1]):
            dist = vector_difference(head, tail)
            if np.sqrt(dist.x**2+dist.y**2) < 2:
                continue
            else:
                move(Node(np.clip(dist.x, -1, 1), np.clip(dist.y, -1, 1)), tail)
                
        if not (tails[-1].x, tails[-1].y) in visited_pos:
            visited_pos.append((tails[-1].x, tails[-1].y))

print(len(visited_pos))  
        


        
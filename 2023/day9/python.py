with open("input.txt") as f:
    data = f.read().splitlines()

def lower_level(level):
    return [int(level[i+1])-int(level[i]) for i, _ in enumerate(level[:-1])]

out1 = 0
out2 = 0
for line in data:
    line = line.split(" ")
    pyramid = []
    pyramid.append(line)
    numbers_different = True
    while numbers_different:
        pyramid.append(lower_level(pyramid[-1]))
        if len(set(pyramid[-1])) == 1:
            numbers_different = False
    for i, level in enumerate(reversed(pyramid[0:len(pyramid)-1])):
        real_i = len(pyramid) - i - 2
        pyramid[real_i].append(int(pyramid[real_i][-1]) + int(pyramid[real_i+1][-1]))
        pyramid[real_i].insert(0, int(pyramid[real_i][0]) - int(pyramid[real_i+1][0]))
    out1 += pyramid[0][-1]
    out2 += pyramid[0][0]

print(out1)
print(out2)
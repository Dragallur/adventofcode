with open("input.txt") as f:
    data = f.read().splitlines()

cycle = 0
x_register = 1
sprite_pos = [0, 1, 2]
s = ""
rel_cycle = dict.fromkeys([20, 60, 100, 140, 180, 220])
str_cycle = [40, 80, 120, 160, 200, 240]

def incr_cycle(cycle, s, sprite_pos):
    if cycle % 40 in sprite_pos:
        s += "#"
    else:
        s += "."
    cycle += 1

    if cycle in rel_cycle:
        rel_cycle[cycle] = x_register *  cycle

    if cycle in str_cycle:
        print(s)
        s = ""
    return cycle, s, sprite_pos

for line in data:
    if line == "noop":
        cycle, s, sprite_pos = incr_cycle(cycle, s, sprite_pos)
    else:
        cycle, s, sprite_pos = incr_cycle(cycle, s, sprite_pos)
        cycle, s, sprite_pos = incr_cycle(cycle, s, sprite_pos)
        x_register += int(line.split(" ")[1])
        sprite_pos = [x+int(line.split(" ")[1]) for x in sprite_pos]

print(sum(rel_cycle.values()))


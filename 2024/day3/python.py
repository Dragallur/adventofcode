with open("2024/day3/input.txt") as f:
    d = f.read()

i = 0
res = 0
enabled = True
while i < len(d):
    if d[i:i+4] == 'mul(':
        ind = d.find(')', i+7)
        spl = d[i+4:ind].split(',')
        if len(spl) == 2 and spl[0].isdigit() and spl[1].isdigit():
            if enabled:
                res += int(spl[0]) * int(spl[1])
            i += 7
            continue
    if d[i:i+4] == 'do()':
        enabled = True
        i += 4
        continue
    if d[i:i+7] == "don't()":
        enabled = False
        i += 7
    i += 1

print(res)

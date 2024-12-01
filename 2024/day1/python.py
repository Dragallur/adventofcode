with open("2024/day1/input.txt") as f:
    data = f.read().splitlines()

left_col = [int(x.split('   ')[0]) for x in data]
right_col = [int(x.split('   ')[1]) for x in data]

left_col = sorted(left_col)
right_col = sorted(right_col)

distances = [abs(l-r) for l, r in zip(left_col, right_col)]

print('Part one:', sum(distances))

memory = {}
def count_occurences(number, l):
    if number in memory:
        return memory[number]

    res = sum([number == x for x in l])
    memory[number] = res
    return res

occurences = [count_occurences(n, right_col) for n in left_col]

sim_score = [l * occu for l, occu in zip(left_col, occurences)]

print('Part two:', sum(sim_score))
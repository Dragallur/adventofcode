import numpy as np

with open("2024/day2/input.txt") as f:
    data = f.read().splitlines()

data = [np.array(line.split()).astype(int) for line in data]
d_lambda = lambda arr: arr[:-1] - arr[1:]
diff = [d_lambda(d) for d in data]
r1 = lambda arr: np.all(arr > 0) or np.all(arr < 0)
r2 = lambda arr: np.all(np.abs(arr) < 4) 
incr_decr = [r1(d) for d in diff]
at_most_three = [r2(d) for d in diff]
res = [a and b for a, b in zip(incr_decr, at_most_three)]
print('First part:', sum(res))

corr = 0
for i, r in enumerate(res):
    if r:
        continue
    temp = data[i].copy()
    for j in range(data[i].size):
        temp2 = np.concatenate((temp[:j], temp[np.clip(j+1, None, data[i].size):]))
        d_temp2 = d_lambda(temp2)
        if r1(d_temp2) and r2(d_temp2):
            corr += 1
            break

print('Second part', corr + sum(res))
import numpy as np

with open("2022/day8/input.txt") as f:
    data = f.read().splitlines()

arr = np.empty((len(data),len(data[0])))
for i, line in enumerate(data):
    arr[i] = list(line)

sizes = np.array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

def minmax(arr):
    if arr.size == 0:
        return np.inf, -np.inf
    mi = np.min(arr)
    ma = np.max(arr)
    return mi, ma

def search_rows(arr):
    list_of_trees = []
    for row in range(np.shape(arr)[0]):
        r = [np.inf, -np.inf]
        for i in sizes:
            r_temp = minmax(np.argwhere(arr[row,:] == i))
            if r_temp[0] < r[0]:
                r[0] = r_temp[0]
                list_of_trees.append([row, r_temp[0]])
            if r_temp[1] > r[1]:
                r[1] = r_temp[1]
                list_of_trees.append([row, r_temp[1]])
    return np.array(list_of_trees)

res = np.unique(np.concatenate((search_rows(arr), search_rows(arr.T)[:, [1, 0]])), axis=0)
print(len(res))

#not trying to be efficient anymore, 2nd part is too different to what I programmed

def one_direction(vec, a_ma):
    res = 0
    for i in range(len(vec)):
        res += 1
        if vec[i] >= a_ma:
            return res
    return res

scenery = np.empty_like(arr)
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        left = one_direction(np.flip(arr[i,:j]), arr[i,j])
        right = one_direction(arr[i,j+1:], arr[i,j])
        up = one_direction(np.flip(arr[:i,j]), arr[i,j])
        down = one_direction(arr[i+1:,j], arr[i,j])
        scenery[i, j] = left * right * up * down

print(np.max(scenery))
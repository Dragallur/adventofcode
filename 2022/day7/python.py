import numpy as np

file = open("2022/day7/input.txt", "r")
data = file.readlines()

class Folder:
    def __init__(self, parent_folder, name):
        self.name = name
        self.parent_folder = parent_folder
        self.files = {}
        self.child_folders = {}

folders = {}
folders["/"] = Folder(None, "/")
current_folder = folders["/"]
num_of_dir = 0

for i, line in enumerate(data[1:]):
    line = line.strip()
    if line[0] == "$":
        if line[2:4] == "cd":
            if line[5:] == "..":
                current_folder = current_folder.parent_folder
            else:
                current_folder = current_folder.child_folders[line[5:]]
    if line[0:3] == "dir":
        if line[4:] not in current_folder.child_folders:
            num_of_dir += 1
            current_folder.child_folders[line[4:]] = Folder(current_folder, line[4:])
            folders[line[4:] + " " + str(i)] = current_folder.child_folders[line[4:]]
    if line[0].isdigit():
        l = line.split()
        current_folder.files[l[1]] = int(l[0])

def traverse(folder):
    list_of_child_folders = list(folder.child_folders.values())
    for child in list_of_child_folders:
        for size in traverse(child):
            yield size 
    yield sum(folder.files.values())

res = []
res2 = [None, np.inf]
for folder_name, folder in folders.items():
    size = np.array([x for x in traverse(folder)])
    if sum(size) <= 100000:
        res.append(sum(size))

    if folder_name == "/":
        total_used_space = sum(size)
        free_space = 70000000 - total_used_space
        space_to_be_free = 30000000 - free_space
    
    if sum(size) >= space_to_be_free:
        if sum(size) < res2[1]:
            res2 = [folder_name, sum(size)]

print(sum(res))
print(res2[1])
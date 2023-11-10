import numpy as np

file = open("2022/day6/input.txt", "r")
s = str(file.readlines()[0])
#s = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

mult4 = len(s) // 4
mult14 = len(s) // 14
code = [None] * 4
message = [None] * 14
start_found = False
message_found = False

for i in range(len(s)):
    ind = i % 4
    ind2 = i % 14
    code[ind] = s[i]
    message[ind2] = s[i]
    if len(set(code)) == 4 and None not in code and not start_found:
        res1 = i + 1
        start_found = True

    if len(set(message)) == 14 and None not in message and not message_found:
        res2 = i + 1
        message_found = True


print(res1, res2)
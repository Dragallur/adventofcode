import numpy as np
import re

with open("2023/day1/input.txt") as f:
    data = f.read().splitlines()

re_first1 = r"(\d)"
re_last1 = r"(\d)(?:[^\d]*)$"

out1 = [int(re.search(re_first1, x)[0] +
       re.search(re_last1, x)[1]) for x in data]

print(sum(out1))

num_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
            "seven": 7, "eight": 8, "nine": 9, "1": 1, "2": 2, "3": 3, "4": 4,
            "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

re_first2 = r"(\d|one|two|three|four|five|six|seven|eight|nine)"
re_last2 = r"(\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)"

out2_first = [re.search(re_first2, x)[0] for x in data]
out2_first = [str(num_dict.get(x)) for x in out2_first]
out2_last = [re.search(re_last2, x[::-1])[0][::-1] for x in data]
out2_last = [str(num_dict.get(x)) for x in out2_last]

out2 = list(map(''.join, zip(out2_first, out2_last)))
print(sum([int(x) for x in out2]))
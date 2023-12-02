with open("2023/day2/input.txt") as f:
    data = f.read().splitlines()

actual_content = {"red": 12, "green": 13, "blue": 14}
max_for_game = {"red": 0, "green": 0, "blue": 0}
ids = list(range(1, len(data)+1))
out2 = 0

for id_game, line in enumerate(data):
    max_for_game["red"] = max_for_game["green"] = max_for_game["blue"] = 0
    for i, turn in enumerate(line.split(":")[1].split(";")):
        for color in turn.split(","):
            color_split = color.split(" ")
            color_split[:] = [x for x in color_split if x]
            max_for_game[color_split[1]] = max(int(color_split[0]), 
                                               max_for_game[color_split[1]])
            if int(color_split[0]) > actual_content[color_split[1]]:
                ids[id_game] = 0
    out2 += max_for_game["red"] * max_for_game["green"] * max_for_game["blue"]
        
print(sum(set(ids)))
print(out2)
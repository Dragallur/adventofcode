#does not work for the first part since I rebuild it too much though it was trivial so who cares,
#also there are some remnants like the lambda function that are not needed anymore
with open("input.txt") as f:
    data = f.read().splitlines()

part2 = True

class Item:
    def __init__(self, value):
        self.value = value
        self.divisibles = {}

class Monkey:
    def __init__(self, id, st_items, operation, operation_type, operation_value, test, test_T, test_F):
        self.id = id
        self.items = [Item(int(i)) for i in st_items]
        self.operation = operation
        self.operation_type = operation_type
        self.operation_value = operation_value
        self.test = test
        self.test_T = test_T
        self.test_F = test_F
        self.n_inspections = 0

def create_lambda_function(expression):
    return lambda old: eval(expression)

monkey_list = []
for i, line in enumerate(data):
    if line.startswith("Monkey"):
        monkey_list.append(Monkey(
            int(data[i][-2]), 
            data[i+1].split(":")[1].split(","),
            create_lambda_function(data[i+2].split("=")[1]),
            data[i+2].split(" ")[-2],
            data[i+2].split(" ")[-1],
            int(data[i+3].split(" ")[-1]),
            int(data[i+4][-1]),
            int(data[i+5][-1])
        ))

def monkey_turn(monkey):
    if monkey.items == []:
        return
    
    for id, _ in enumerate(monkey.items):
        monkey.n_inspections += 1
        if monkey.operation_type == "+":
            for div in monkey.items[id].divisibles:
                monkey.items[id].divisibles[div] += int(monkey.operation_value)

        if monkey.operation_type == "*":
            if monkey.operation_value != "old":
                for div in monkey.items[id].divisibles:
                    monkey.items[id].divisibles[div] *= int(monkey.operation_value)
            else:
                for div in monkey.items[id].divisibles:
                    monkey.items[id].divisibles[div] = monkey.items[id].divisibles[div]**2 % int(div)

        for div in monkey.items[id].divisibles:
            if monkey.items[id].divisibles[div] >= int(div):
                monkey.items[id].divisibles[div] = monkey.items[id].divisibles[div] % int(div)

        if monkey.items[id].divisibles[monkey.test] == 0:
            monkey_list[monkey.test_T].items.append(monkey.items[id])
        else:
            monkey_list[monkey.test_F].items.append(monkey.items[id])


    monkey.items = []

def one_round():
    for monkey in monkey_list:
        monkey_turn(monkey)

all_test_values = [monkey.test for monkey in monkey_list]
for monkey in monkey_list:
    for id, _ in enumerate(monkey.items):
        for test_value in all_test_values:
            monkey.items[id].divisibles[test_value] = int(monkey.items[id].value) % int(test_value)

for i in range(10000):
    one_round()


inspections = [monkey.n_inspections for monkey in monkey_list]
inspections.sort(reverse=True)
print(inspections[0]*inspections[1])

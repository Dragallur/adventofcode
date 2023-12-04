with open("input.txt") as f:
    data = f.read().splitlines()

cards_sum = [None] * len(data)
num_of_cards = [1] * len(data)

for id, line in enumerate(data):
    win_cards, your_cards = line.split(":")[1].split("|")
    
    cards_sum[id] = sum([True for x in your_cards.split(" ") if x != "" and x in win_cards.split(" ")])
    num_of_cards[id+1:(id+1+cards_sum[id])] = [sum(x) for x in 
                                               zip(num_of_cards[id+1:(id+1+cards_sum[id])] ,[num_of_cards[id]] * cards_sum[id])]

print(sum([2**(int(x)-1) for x in cards_sum if x > 0]))
print(sum(num_of_cards))
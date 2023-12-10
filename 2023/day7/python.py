import numpy as np

with open("input.txt") as f:
    data = f.read().splitlines()

card_strength = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
type_strength = ["high", "one", "two", "three", "full", "four", "five"]
part2 = True
if part2:
    card_strength = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

def four_or_full(cards):
    count = cards.count(cards[0])
    if count == 1 or count == 4:
        return "four"
    elif count == 2 or count == 3:
        return "full"
    return None

def three_or_two(hand):
    count1 = hand.count(hand[0])
    count2 = hand.count(hand[1])
    if count1 == 2 or count2 == 2:
        return "two"
    else:
        return "three"

def get_type(hand):
    l = len(set(hand))
    match l:
        case 1: return "five"
        case 2: return four_or_full(hand)
        case 3: return three_or_two(hand)
        case 4: return "one"
        case 5: return "high"
        case _: return None

def highest_card(hand1, hand2, ind = 0):
    if hand1[ind] == hand2[ind]:
        ind += 1
        return highest_card(hand1, hand2, ind)
    else:
        if card_strength.index(hand1[ind]) > card_strength.index(hand2[ind]):
            return hand1
        else:
            return hand2

def change_type(hand, hand_type):
    count_J = hand.count("J")    
    match count_J:
        case 0: return hand_type
        case 1: 
            match hand_type:
                case "four": return "five"
                case "three": return "four"
                case "two": return "full"
                case "one": return "three"
                case "high": return "one"
                case _: return None
        case 2:
            match hand_type:
                case "full": return "five"
                case "two": return "four"
                case "one": return "three"
                case _: return None
        case 3:
            match hand_type:
                case "full": return "five"
                case "three": return "four"
                case _: return None
        case 4:
            return "five"
        case _:
            return hand_type

def compare_two_hands(hand1, hand2):
    type1, type2 = get_type(hand1), get_type(hand2)
    if part2:
        type1, type2 = change_type(hand1, type1), change_type(hand2, type2)
    strength1, strength2 = type_strength.index(type1), type_strength.index(type2)
    if strength1 > strength2:
        return hand1
    elif strength1 < strength2:
        return hand2
    else:
        return highest_card(hand1, hand2)
            
def bubble_sort(data):
    l = len(data)
    swap = True
    while swap:
        swap = False 
        l -= 1
        for i in range(l):
            hand1, hand2 = data[i].split(" ")[0], data[i+1].split(" ")[0]
            if compare_two_hands(hand1, hand2) == hand1:
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp
                swap = True
    return data

data = bubble_sort(data)
total_winnings = 0

for i, line in enumerate(data):
    bid = line.split(" ")[1]
    total_winnings += (i+1) * int(bid)

print(total_winnings)
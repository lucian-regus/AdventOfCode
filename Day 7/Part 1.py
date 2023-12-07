#!/usr/bin/env python3

cards = {line[0]: line[1] for line in [line.strip().split() for line in open("input.txt")]}
ranking = [[] for _ in range(7)]
order = {'A': 0, 'K': 1, 'Q': 2, 'J': 3, 'T': 4, '9': 5, '8': 6, '7': 7, '6': 8, '5': 9, '4': 10, '3': 11, '2': 12}

def checker(card):
    map = {}
    for char in card:
        if char in map:
            map[char] += 1
        else:
            map[char] = 1
    cardList = sorted(list(map.items()), key=lambda x: x[1], reverse=True)

    if cardList[0][1] == 5:
        ranking[6].append(card)
        return
    if cardList[0][1] == 4:
        ranking[5].append(card)
        return
    if cardList[0][1] == 3 and cardList[1][1] == 2:
        ranking[4].append(card)
        return
    if cardList[0][1] == 3:
        ranking[3].append(card)
        return
    if cardList[0][1] == 2 and cardList[1][1] == 2:
        ranking[2].append(card)
        return
    if cardList[0][1] == 2:
        ranking[1].append(card)
        return
    if cardList[0][1] == 1:
        ranking[0].append(card)
        return

for card, values in cards.items():
    checker(card)

for index, card in enumerate(ranking):
    ranking[index] = sorted(card, key=lambda x: [order[char] for char in x], reverse=True)

output = sum(ranking, [])
sum = 0
for index,i in enumerate(output):
    sum += int(cards[i]) * (index + 1)
print(sum)
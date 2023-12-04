#!/usr/bin/env python3
import re

cards = list(open('input.txt'))
numOf = [1 for _ in range(len(cards))]
total_sum = 0

for cardNumber, card in enumerate(cards):
    tmpWorth = 0
    counter = 0
    cardNumber = int(re.findall(r'\d+(?=:)', card)[0])
    card = card[card.find(':')+2:]

    winning_numbers, your_numbers = map(str.split, card.split(" | "))

    for number in map(int, your_numbers):
        if str(number) in winning_numbers:
            counter += 1
            if tmpWorth == 0:
                tmpWorth = 1
            else:
                tmpWorth *= 2
    value = numOf[cardNumber - 1]
    for i in range(cardNumber, cardNumber + counter):
        numOf[i] += value

total_sum = sum(numOf)

print(total_sum)

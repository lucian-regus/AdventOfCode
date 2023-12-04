#!/usr/bin/env python3

cards = list(open('input.txt'))
output = 0

for card in cards:
	worth = 0
	card = card[card.find(':')+2:]

	winning_numbers, your_numbers = map(str.split, card.split(" | "))

	for number in map(int, your_numbers):
	    if str(number) in winning_numbers:
	    	if worth == 0:
	    		worth = 1
	    	else:
	    		worth *= 2
	output += worth
print(output)

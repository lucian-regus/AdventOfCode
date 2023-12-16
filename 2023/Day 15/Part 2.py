#!/usr/bin/env python3
import re

def hash(string):
    value = 0
    for char in string:
        value += ord(char)
        value *= 17
        value %= 256
    return value

def inBoxes(boxNum, letters):
    if boxNum in boxes:
        val = boxes[boxNum]
        if letters in val:
            return True
    return False

pattern = re.compile(r'([a-zA-Z]+)(=|-)(\d+)?')
data = open('input.txt').read().split(',')

boxes = {}
for string in data:
    match = pattern.match(string)

    if match:
        letters = match.group(1)
        symbol = match.group(2)
        number = match.group(3)

        box = hash(letters)
        if symbol == '=':
            if inBoxes(box, letters):
                boxes[box][letters] = int(number)
            else:
                if box in boxes:
                    boxes[box][letters] = int(number)
                else:
                    boxes[box] = {letters: int(number)}
        elif symbol == '-':
            if inBoxes(box, letters):
                boxes[box].pop(letters)
                if not boxes[box]:
                	boxes.pop(box)
output = 0
for outerBox, innerBoxDict in boxes.items():
	slot = 1
	for innerBox, innerBoxValue in innerBoxDict.items():
		value = (outerBox + 1) * slot * innerBoxValue
		slot += 1
		output += value
print(output)
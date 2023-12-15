#!/usr/bin/env python3

inputMap = [list(line.strip()) for line in open('input.txt')]

def moveO(row, column):
    while 0 < row and inputMap[row-1][column] != '#' and inputMap[row-1][column] == '.':
        row -= 1
    inputMap[row][column] = 'O'

output = 0

for row in range(0, len(inputMap)):
    for column in range(0, len(inputMap[0])):
        if inputMap[row][column] == 'O':
            inputMap[row][column] = '.'
            moveO(row, column)

for row in range(0, len(inputMap)):
    for column in range(0, len(inputMap[0])):
    	if inputMap[row][column] == 'O':
    		output += len(inputMap) - row

print(output)

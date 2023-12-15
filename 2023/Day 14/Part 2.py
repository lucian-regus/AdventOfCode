#!/usr/bin/env python3

inputMap = [list(line.strip()) for line in open('input.txt')]

def moveNorth(row, column):
    while 0 < row and inputMap[row-1][column] != '#' and inputMap[row-1][column] == '.':
        row -= 1
    inputMap[row][column] = 'O'

def moveWest(row, column):
    while 0 < column and inputMap[row][column-1] != '#' and inputMap[row][column-1] == '.':
        column -= 1
    inputMap[row][column] = 'O'

def moveSouth(row, column):
    while row < len(inputMap) - 1 and inputMap[row+1][column] != '#' and inputMap[row+1][column] == '.':
        row += 1
    inputMap[row][column] = 'O'

def moveEast(row, column):
    while column < len(inputMap[0]) - 1 and inputMap[row][column+1] != '#' and inputMap[row][column+1] == '.':
        column += 1
    inputMap[row][column] = 'O'

output = 0

def cycles():
    for i in range(1000000000):
        print(i)
        for row in range(0, len(inputMap)):
            for column in range(0, len(inputMap[0])):
                if inputMap[row][column] == 'O':
                    inputMap[row][column] = '.'
                    moveNorth(row, column)

        for row in range(0, len(inputMap)):
            for column in range(0, len(inputMap[0])):
                if inputMap[row][column] == 'O':
                    inputMap[row][column] = '.'
                    moveWest(row, column)

        for row in range(len(inputMap) - 1, -1, -1):
            for column in range(0, len(inputMap[0])):
                if inputMap[row][column] == 'O':
                    inputMap[row][column] = '.'
                    moveSouth(row, column)

        for row in range(len(inputMap) - 1, -1, -1):
            for column in range(len(inputMap[0]) - 1, -1, -1):
                if inputMap[row][column] == 'O':
                    inputMap[row][column] = '.'
                    moveEast(row, column)

cycles()

for row in range(0, len(inputMap)):
    for column in range(0, len(inputMap[0])):
        if inputMap[row][column] == 'O':
            output += len(inputMap) - row

print(output)

#!/usr/bin/env python3
inputMap = []

output = 0

def checkHorizontal():
    global output
    for row in range(0, len(inputMap) - 1):
        flag = True
        for column in range(0, len(inputMap[row])):
            if inputMap[row][column] != inputMap[row + 1][column]:
                flag = False
                break
        if flag:
            if checkHorizontalReflection(row, row + 1):
                output += (row + 1) * 100

def checkHorizontalReflection(row, nextRow):
    for offset in range(1, 10):
        if 0 <= row - offset and len(inputMap) > nextRow + offset:
            for column in range(0, len(inputMap[row])):
                if inputMap[row - offset][column] != inputMap[nextRow + offset][column]:
                    return False
    return True

def checkVertical():
    global output
    for column in range(0, len(inputMap[0]) - 1):
        flag = True
        for row in range(0, len(inputMap) - 1):
            if inputMap[row][column] != inputMap[row][column + 1]:
                flag = False
                break
        if flag:
            if checkVerticalReflection(column, column + 1):
                output += column + 1


def checkVerticalReflection(column, nextColumn):
    for row in range(0, len(inputMap)):
        for offset in range(0, 10):
            if 0 <= column - offset and len(inputMap[0]) > nextColumn + offset:
                if inputMap[row][column - offset] != inputMap[row][nextColumn + offset]:
                    return False
    return True

def printMap():
    for row in inputMap:
        print(row)

with open("input.txt", 'r') as file:
    while True:
        line = file.readline()

        if not line:
            printMap()
            checkHorizontal()
            checkVertical()
            break
        stripped_line = line.strip()

        if not stripped_line:
            printMap()
            checkHorizontal()
            checkVertical()
            inputMap.clear()
            continue
        inputMap.append([char for char in stripped_line])
print(output)

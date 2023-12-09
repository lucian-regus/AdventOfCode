#!/usr/bin/env python3

matrix = [list(line.strip()) for line in open("input.txt", 'r')]
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
sum = 0
numbers = set()

def isValid(x, y):
    return 0 <= x < len(matrix[0]) and 0 <= y < len(matrix)

def createNumber(x, y):
    tmp = 0
    while isValid(x, y) and matrix[y][x].isdigit():
        x -= 1
    x += 1
    while isValid(x, y) and matrix[y][x].isdigit():
        tmp = tmp * 10 + int(matrix[y][x])
        x += 1
    numbers.add(tmp)

for y in range(len(matrix)):
    for x in range(len(matrix[y])):
        if matrix[y][x] == '*':
            for dy, dx in directions:
                tmpX = x + dx
                tmpY = y + dy
                if isValid(tmpX, tmpY) and matrix[tmpY][tmpX].isdigit():
                    createNumber(tmpX, tmpY)
            
            if len(numbers) == 2:
                ratio = 1
                for i in numbers:
                    ratio *= i
                sum += ratio
            numbers.clear()

print(sum)

#!/usr/bin/env python3
total_sum = 0

def isValid(x, y):
    return 0 <= x < len(matrix) and 0 <= y < len(matrix)
def createNumber(firstX, lastX, y):
    number = 0
    for x in range(firstX, lastX + 1):
        number = number * 10 + int(matrix[y][x])
    return number
def check_adjacency(firstX, lastX, y):
    global total_sum
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for x in range(firstX, lastX + 1):
        for dy, dx in directions:
            tmpX = x + dx
            tmpY = y + dy
            if isValid(tmpX, tmpY) and not matrix[tmpY][tmpX].isdigit() and matrix[tmpY][tmpX] != '.':
                total_sum += createNumber(firstX, lastX, y)
                return

matrix = [list(line.strip()) for line in open("input.txt", 'r')]


for y in range(len(matrix)):
    firstX = -1
    lastX = -1
    for x in range(len(matrix[y])):
        if matrix[y][x].isdigit() and not matrix[y][x + 1].isdigit() if x + 1 < len(matrix[y]) else True:
            lastX = x
        if matrix[y][x].isdigit() and firstX == -1:
            firstX = x
            continue
        if firstX != -1 and lastX != -1:
            check_adjacency(firstX, lastX, y)
            firstX = -1
            lastX = -1

print(total_sum)

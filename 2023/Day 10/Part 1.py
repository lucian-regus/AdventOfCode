#!/usr/bin/env python3

map = [list(line.strip()) for line in open('input.txt')]

startX = startY = 0
currentX = currentY = 0
lastX = lastY = 0
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def findS():
    global startX, startY,lastX,lastY
    for row, i in enumerate(map):
        for column, j in enumerate(i):
            if j == 'S':
                startX = lastX = column
                startY = lastY = row
                return

def isValid(x, y):
    return 0 <= x < len(map[0]) and 0 <= y < len(map)

def firstPoz():
    global currentX, currentY
    for index, (dy, dx) in enumerate(directions):
        tmpX = startX + dx
        tmpY = startY + dy
        if isValid(tmpX, tmpY):
            if index == 0:
                if map[tmpY][tmpX] == '7':
                    currentX = tmpX
                    currentY = tmpY
                    return
                if map[tmpY][tmpX] == '|':
                    currentX = tmpX
                    currentY = tmpY
                    return
                if map[tmpY][tmpX] == 'F':
                    currentX = tmpX
                    currentY = tmpY
                    return
            if index == 1:
                if map[tmpY][tmpX] == '7':
                    currentX = tmpX
                    currentY = tmpY
                    return
                if map[tmpY][tmpX] == 'J':
                    currentX = tmpX
                    currentY = tmpY
                    return
                if map[tmpY][tmpX] == '-':
                    currentX = tmpX
                    currentY = tmpY
                    return
            if index == 2:
                if map[tmpY][tmpX] == '|':
                    currentX = tmpX
                    currentY = tmpY
                    return
                if map[tmpY][tmpX] == 'J':
                    currentX = tmpX
                    currentY = tmpY
                    return
                if map[tmpY][tmpX] == 'L':
                    currentX = tmpX
                    currentY = tmpY
                    return
            if index == 3:
                if map[tmpY][tmpX] == '-':
                    currentX = tmpX
                    currentY = tmpY
                    return
                if map[tmpY][tmpX] == 'F':
                    currentX = tmpX
                    currentY = tmpY
                    return

def getDirection():
    global currentX,currentY,lastY,lastX
    if map[currentY][currentX] == '|':
        if lastY == currentY - 1 and lastX == currentX:
            lastY = currentY
            currentY = currentY + 1
            return
        if lastY == currentY + 1 and lastX == currentX:
            lastY = currentY
            currentY = currentY - 1
            return
    if map[currentY][currentX] == '-':
        if lastX == currentX - 1 and lastY == currentY:
            lastX = currentX
            currentX = currentX + 1
            return
        if lastX == currentX + 1 and lastY == currentY:
            lastX = currentX
            currentX = currentX - 1
            return
    if map[currentY][currentX] == 'L':
        if lastY == currentY - 1 and lastX == currentX:
            lastY = currentY
            currentX = currentX + 1
            return
        if lastX == currentX + 1 and lastY == currentY:
            lastX = currentX
            currentY = currentY - 1
            return
    if map[currentY][currentX] == 'J':
        if lastY == currentY - 1 and lastX == currentX:
            lastY = currentY
            currentX = currentX - 1
            return
        if lastX == currentX - 1 and lastY == currentY:
            lastX = currentX
            currentY = currentY - 1
            return
    if map[currentY][currentX] == '7':
        if lastX == currentX - 1 and lastY == currentY:
            lastX = currentX
            currentY = currentY + 1
            return
        if lastY == currentY + 1 and lastX == currentX:
            lastY = currentY
            currentX = currentX - 1
            return
    if map[currentY][currentX] == 'F':
        if lastY == currentY + 1 and lastX == currentX:
            lastY = currentY
            currentX = currentX + 1
            return
        if lastX == currentX + 1 and lastY == currentY:
            lastX = currentX
            currentY = currentY + 1
            return

findS()
firstPoz()

output = 1
while True:
	getDirection()
	output += 1
	if currentX == startX and currentY == startY:
		break
print(int(output/2))
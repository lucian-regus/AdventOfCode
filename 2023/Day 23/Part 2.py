#!/usr/bin/env python3

inputMap = [list(line.strip()) for line in open('input.txt')]

startY = ''.join(inputMap[0]).find('.')
startX = 0
finishY = ''.join(inputMap[len(inputMap)-1]).find('.')
finishX = len(inputMap)-1

directions = ((0,1),(0,-1),(1,0),(-1,0))

def isValid(x, y):
    return 0 <= x < len(inputMap) and 0 <= y < len(inputMap[0])

def move(x,y,parentVisited):
	currentX = x
	currentY = y
	length = 1
	childVisited = parentVisited.copy()
	while True:
		counter = 0
		available = set()
		for dX,dY in directions:
			if isValid(currentX+dX,currentY+dY) and inputMap[currentX+dX][currentY+dY] !='#' and (currentX+dX,currentY+dY) not in childVisited:
				counter += 1
				available.add((dX,dY))
			
		childVisited.add((currentX,currentY))

		if currentX == finishX and currentY == finishY:
			return length

		if counter == 0:
			return -1

		if counter == 1:
			for dX,dY in available:
				currentX += dX
				currentY += dY
			length += 1

		if counter > 1:
			maxLength = -1
			for dX,dY in available:
				tmpLength = move(currentX+dX,currentY+dY,childVisited)
				if tmpLength > maxLength:
					maxLength = tmpLength
			return length+maxLength

visited = set()
print(move(startX,startY,visited)-1)
#!/usr/bin/env python3
from math import lcm

with open("input.txt",'r') as file:
	global path
	global pathMap
	global currentPositions
	pathMap = {}
	currentPositions = []

	line = file.readline()
	path = line.strip()

	while line:
		line = file.readline()
		if line.strip() != '':
			parts = line.strip().split(" = ")
			if(parts[0][-1] == 'A'):
				currentPositions.append(parts[0])
			pathMap[parts[0]] = list(map(str, parts[1].replace('(','').replace(')','').split(', ')))

outputs = []
for key in currentPositions:
	currentPosition = key
	counter = 0
	while currentPosition[-1] != 'Z':
		for char in path:
			if char == 'L':
				currentPosition = pathMap[currentPosition][0]
				counter += 1
			else:
				currentPosition = pathMap[currentPosition][1]
				counter += 1
	outputs.append(counter)
print(lcm(*outputs))
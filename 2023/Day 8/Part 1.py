#!/usr/bin/env python3


with open("input.txt",'r') as file:
	global path
	global pathMap
	pathMap = {}

	line = file.readline()
	path = line.strip()

	while line:
		line = file.readline()
		if line.strip() != '':
			parts = line.strip().split(" = ")
			pathMap[parts[0]] = list(map(str, parts[1].replace('(','').replace(')','').split(', ')))


currentPosition = "AAA"
output = 0
while currentPosition != "ZZZ":
	for char in path:
		if char == 'L':
			currentPosition = pathMap[currentPosition][0]
			output += 1
		else:
			currentPosition = pathMap[currentPosition][1]
			output += 1
print(output)

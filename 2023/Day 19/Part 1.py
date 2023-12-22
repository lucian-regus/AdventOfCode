#!/usr/bin/env python3

import re

workflows = {}
parts = []

def readInput():
	global parts
	with open("input.txt", 'r') as file:
		flag = False
		while True:
			line = file.readline().strip()

			if not line and flag == False:
				flag = True
				continue
			if not line and flag == True:
				break

			if flag == False:
				tmp = line.split('{')
				tmp[1] = tmp[1][:-1]
				workflows[tmp[0]] = tmp[1].split(',')
			else:
				parts.append(line[1:-1])

def checker():
	currentRule = "in"
	while currentRule != 'R' and currentRule != 'A':
		values = workflows[currentRule]
		for value in values:
			if '<' in value or '>' in value:
				rule = re.split(r'<|>|:', value)
				sign = value[1]
				if sign == '<':
					if int(part[rule[0]]) < int(rule[1]):
						currentRule = rule[2]
						break
					else:
						continue
				if sign == '>':
					if int(part[rule[0]]) > int(rule[1]):
						currentRule = rule[2]
						break
					else:
						continue
			else:
				currentRule = value
	return currentRule
readInput()

part = {}
output = 0
for line in parts:
	elements = line.split(',')
	tmpSum = 0
	for element in elements:
		tmp = element.split('=')
		part[tmp[0]] = tmp[1]
		tmpSum += int(tmp[1])
	result = checker()
	if result == 'A':
		output += tmpSum

print(output)

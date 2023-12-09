#!/usr/bin/env python3
import re

with open("input.txt", 'r') as file:
	line = file.readline()
	numbers = ["one","two","three","four","five","six","seven","eight","nine"]
	sum = 0
	while line:
		line = re.sub(r'(two|three)',r't\1',line)
		line = re.sub(r'(eight)',r'e\1',line)
		line = re.sub(r'(nine)',r'n\1',line)
		line = re.sub(r'(one)',r'o\1',line)
		for index,number in enumerate(numbers):
			line = line.replace(number,str(index + 1))
		tmp = None

		for char in line:
			if char.isdigit():
				tmp = int(char)
				break
		for char in reversed(line):
			if char.isdigit():
				tmp = tmp * 10 + int(char)
				break
		sum = sum + tmp
		line = file.readline()

print(sum)
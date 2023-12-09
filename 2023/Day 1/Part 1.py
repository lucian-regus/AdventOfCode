#!/usr/bin/env python3

with open("input.txt", 'r') as file:
	line = file.readline()
	sum = 0
	while line:
		tmp = None

		for char in line:
			if char.isdigit():
				tmp = int(char)
				break
		for char in reversed(line):
			if char.isdigit():
				tmp = tmp * 10 +  int(char)
				break

		sum = sum + tmp
			
		line = file.readline()
	print(sum)

#!/usr/bin/env python3


def hash(string):
	value = 0
	for char in string:
		value += ord(char)
		value *= 17
		value %= 256
	return value

data = open('input.txt').read().split(',')

output = 0	
for string in data:
	output += hash(string)
print(output)
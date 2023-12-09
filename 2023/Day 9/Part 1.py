#!/usr/bin/env python3

history = [list(map(int, line.split())) for line in open("input.txt")]

output = 0
for arr in history:
	lastElements = []	
	difference = []
	lastElements.append(arr[-1])
	allNotZero = True
	while allNotZero:
		for index,number in enumerate(arr[:-1]):
			difference.append(arr[index+1]-number)
		arr = difference
		difference = []
		allNotZero = any(element != 0 for element in arr)
		lastElements.append(arr[-1])
	lastElement = 0
	for i in reversed(lastElements[:-1]):
		lastElement += i
	output += lastElement	
print(output)

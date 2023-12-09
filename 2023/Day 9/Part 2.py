#!/usr/bin/env python3

history = [list(map(int, line.split())) for line in open("input.txt")]

output = 0
for arr in history:
	firstElements = []	
	difference = []
	firstElements.append(arr[0])
	allNotZero = True
	while allNotZero:
		for index,number in enumerate(arr[:-1]):
			difference.append(arr[index+1]-number)
		arr = difference
		difference = []
		allNotZero = any(element != 0 for element in arr)
		firstElements.append(arr[0])
	firstElement = 0
	for i in reversed(firstElements[:-1]):
		firstElement = i - firstElement

	output += firstElement	
print(output)

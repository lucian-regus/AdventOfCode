#!/usr/bin/env python3
import re


def loadFile():
    global time
    global distance
    with open("input.txt", 'r') as file:
        line = file.readline()
        time = int(''.join(re.findall(r'\d+', line)))
        line = file.readline()
        distance = int(''.join(re.findall(r'\d+', line)))
loadFile()

numOf = 0
output = 1
for i in range(1,time):
	if (time - i) * i > distance:
		numOf += 1
output *= numOf
	
print(output)
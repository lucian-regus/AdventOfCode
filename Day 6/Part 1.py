#!/usr/bin/env python3
import re

time = []
distance = []

output = 1

def loadFile():
    global time
    global distance
    with open("input.txt", 'r') as file:
        line = file.readline()
        time = list(map(int,re.findall(r'\d+', line)))
        line = file.readline()
        distance = list(map(int,re.findall(r'\d+', line)))
loadFile()

for index,number in enumerate(time):
	numOf = 0
	for i in range(1,number):
		if (number - i) * i > distance[index]:
			numOf += 1
	output *= numOf
	
print(output)
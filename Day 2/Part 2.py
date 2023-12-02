#!/usr/bin/env python3
import re

with open("input.txt", 'r') as file:
    line = file.readline()
    sum = 0

    while line:
        line = line.strip()
        line = re.sub(r'(:)', r'\1;', line).split("; ")
        rgb = [0, 0, 0]

        for i in range(1, len(line)):
            parts = line[i].split(", ")

            for j in parts:
                components = j.split(" ")
                if components[1] == "red" and rgb[0] < int(components[0]):
                    rgb[0] = int(components[0])
                if components[1] == "green" and rgb[1] < int(components[0]):
                    rgb[1] = int(components[0])
                if components[1] == "blue" and rgb[2] < int(components[0]):
                    rgb[2] = int(components[0])

        mul = 1
        for i in rgb:
            mul *= i
        sum += mul
        line = file.readline()

print(sum)

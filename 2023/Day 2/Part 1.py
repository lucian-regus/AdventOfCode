#!/usr/bin/env python3
import re

with open("input.txt", 'r') as file:
    line = file.readline()
    valid = [12, 13, 14]
    sum = 0

    while line:
        line = line.strip()
        line = re.sub(r'(:)', r'\1;', line).split("; ")
        flag = True

        for i in range(1, len(line)):
            rgb = [0, 0, 0]
            parts = line[i].split(", ")

            for j in parts:
                components = j.split(" ")
                if components[1] == "red":
                    rgb[0] += int(components[0])
                if components[1] == "green":
                    rgb[1] += int(components[0])
                if components[1] == "blue":
                    rgb[2] += int(components[0])

            for j in range(0, 3):
                if rgb[j] > valid[j]:
                    flag = False
                    break

        if flag:
            sum += int(line[0].replace(":", "").split(" ")[1])
        line = file.readline()

print(sum)

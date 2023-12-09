#!/usr/bin/env python3
import re

maps = {}
seeds = []

def loadFile():
    global seeds
    with open("input.txt", 'r') as file:
        line = file.readline()
        seeds = list(map(int, re.findall(r'\b\d+\b', line)))

        while line:
            line = file.readline()
            if "map:" in line:
                currentMap = line.strip()[:-1]
                map_lines = []
                line = file.readline()
                while line.strip() != '':
                    map_lines.append(list(map(int, line.split())))
                    line = file.readline()
                map_lines = sorted(map_lines, key=lambda x: x[1])
                maps[currentMap] = map_lines

loadFile()
arrSeeds = []
for index,seed in enumerate(seeds):
    for key, value in maps.items():
        for arr in value:
            if seed >= arr[1] and seed <= (arr[1] + arr[2] - 1):
                seed = seed-arr[1]+arr[0]
                break
    arrSeeds.append(seed)

print(min(arrSeeds))

#!/usr/bin/env python3

grid = [list(line.strip()) for line in open("input.txt")]

empty_rows = []
for i in range(len(grid)):
    if all(x == '.' for x in grid[i]):
        empty_rows.append(i)

empty_cols = []
for i in range(len(grid[0])):
    if all(row[i] == '.' for row in grid):
        empty_cols.append(i) 

galaxies = []
for j in range(len(grid)):
    galaxies.extend([(j, i) for i in range(len(grid[0])) if grid[j][i] == '#'])


def MinMax(a, b):
    return (b, a) if a > b else (a, b)

def solve():
    sum = 0
    for i in range(len(galaxies) - 1):
        (r1, c1) = galaxies[i]
        for j in range(i + 1, len(galaxies)):
            (r2, c2) = galaxies[j]
            d = abs(r1 - r2) + abs(c1 - c2)
            minr, maxr = MinMax(r1, r2)
            minc, maxc = MinMax(c1, c2)
            for er in empty_rows:
                if er > minr and er < maxr:
                    d += 999999

            for ec in empty_cols:
                if ec > minc and ec < maxc:
                    d += 999999
            sum += d
    print(sum)

solve()
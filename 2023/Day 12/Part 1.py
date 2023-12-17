#!/usr/bin/env python3

from functools import cache

@cache
def num_solutions(s, sizes, num_done_in_group=0):
    if not s:
        return not sizes and not num_done_in_group
    output = 0
    possible = [".", "#"] if s[0] == "?" else s[0]
    for c in possible:
        if c == "#":
            output += num_solutions(s[1:], sizes, num_done_in_group + 1)
        else:
            if num_done_in_group:
                if sizes and sizes[0] == num_done_in_group:
                    output += num_solutions(s[1:], sizes[1:])
            else:
                output += num_solutions(s[1:], sizes)
    return output

cases = [l.split() for l in open("input.txt").read().strip().split("\n")]
rows = [(w1, tuple(map(int, w2.split(",")))) for w1, w2 in cases]

output = sum(num_solutions(group + ".", sizes) for group, sizes in rows)
print(output)

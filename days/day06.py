#!/usr/bin/env python3

from functools import reduce
from math import prod

def solve(din):
    lines = din.readlines()
    runs = list(zip(*[map(int, l.split()[1:]) for l in lines]))
    t, d = [int(''.join(l.split()[1:])) for l in lines]
        
    return (
        prod([sum([h * (t - h) > d for h in range(1, t)]) for t, d in runs]),
        sum([h * (t - h) > d for h in range(1, t)]))
        
#!/usr/bin/env python3

from math import lcm

def solve(din):
    commands, __, *paths = din.read().splitlines()
    paths = {p[0:3]: (p[7:10], p[12:15]) for p in paths}
    
    i = 0
    p = 'AAA'
    while p in paths:
        p, i = paths[p][commands[i % len(commands)] == 'R'], i + 1
        if p == 'ZZZ':
            break
        
    j = 0
    ps = [p for p in paths.keys() if p[-1] == 'A']
    loops = []
    while True:
        ps, j = [paths[p][commands[j % len(commands)] == 'R'] for p in ps], j + 1
        pl = len(ps)
        ps = [p for p in ps if p[-1] != 'Z']
        if len(ps) != pl:
            loops.append(j)
        if not ps:
            break
     
    return i, lcm(*loops)
    
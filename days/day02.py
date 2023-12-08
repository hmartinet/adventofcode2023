#!/usr/bin/env python3

import re
from math import prod


def solve(din):
    cubes = ['red', 'green', 'blue']
    limits = [12, 13, 14]
    re_line = re.compile(r'Game (\d+): (.*)')

    def parse_set(s):
        r = [0, 0, 0]
        for v in s.split(','):
            n, c = v.split()
            r[cubes.index(c)] += int(n)
        return r

    def parse_game(g, l):
        return int(g), [parse_set(s) for s in l.split(';')]

    games = [
        parse_game(*re_line.match(l).groups())
        for l in din.readlines()]

    return (
        sum([
            all(min(a - b for a, b in zip(limits, s)) >= 0 for s in sets) and n
            for n, sets in games]),
        sum([
            prod(max(idx) for idx in zip(*sets))
            for __, sets in games]))

#!/usr/bin/env python3

import re
from math import pow


def solve(din):
    re_parse = re.compile(r'Card\s+\d+:([\d\s]+)\|([\d\s]+)')

    def parse_line(l):
        wn, mn = re_parse.match(l).groups()
        return len(set(map(int, wn.split())) & set(map(int, mn.split())))

    cards = list(map(parse_line, din.readlines()))
    hand = list(range(len(cards)))
    for i in iter(hand):
        r, j = cards[i], i + 1
        hand += list(range(j, j + r))

    return (
        sum([int(pow(2, c - 1)) for c in cards]),
        len(hand))

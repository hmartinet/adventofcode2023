import re
from math import prod


def solve(din):
    input = din.readlines()
    symbols = {
        (x, y): [] for x in range(len(input))
        for y in range(len(input[0].strip()))
        if input[x][y] not in '01234566789.'}

    re_digits = re.compile(r'\d+')
    for x, l in enumerate(input):
        for n in re_digits.finditer(l.strip()):
            area = {
                (x, y) for x in (x - 1, x, x + 1)
                for y in range(n.start() - 1, n.end()+1)}

            for o in area & symbols.keys():
                symbols[o].append(int(n.group()))

    return (
        sum(sum(p) for p in symbols.values()),
        sum(prod(p) for p in symbols.values() if len(p) == 2))

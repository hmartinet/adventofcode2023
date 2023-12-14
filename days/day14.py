import re
from functools import cache
from hashlib import sha1

RT = str.maketrans({ord('.'): None})
RH = re.compile('#')
turn = lambda r: list(zip(*r[::-1]))
roll = lambda r: list(map(
    lambda c: [*'#'.join([r.ljust(g, '.') for r, g in rgsplit(c)])], r))
weight = lambda r: sum(map(
    lambda e: e[1] == 'O' and e[0], enumerate(r[::-1], 1)))


@cache
def rgsplit(c):
    s = ''.join(c)
    return list(zip(RH.split(s.translate(RT)), list(map(len, RH.split(s)))))


def solve(din):
    rocks = turn(turn(turn(din.read().splitlines())))
    r1 = sum(map(weight, roll(rocks)))

    i, nf, hlist = 0, 1, []
    while i < 1000000000:
        for __ in range(4):
            rocks = turn(roll(rocks))
        if nf:
            h = sha1(repr(rocks).encode()).digest()
            if h in hlist:
                c = i - hlist.index(h)
                i, nf = ((1000000000 - i) // c) * c + i, 0
            hlist.append(h)
        i += 1
    r2 = sum(map(weight, rocks))

    return r1, r2

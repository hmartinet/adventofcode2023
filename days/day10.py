#!/usr/bin/env python3

from collections import namedtuple

V = namedtuple('Vector', 'x y')


def solve(din):
    MOVES = {
        'S': {V(-1, 0), V(1, 0), V(0, -1), V(0, 1)},
        '|': {V(-1, 0), V(1, 0)},
        '-': {V(0, -1), V(0, 1)},
        'L': {V(-1, 0), V(0, 1)},
        'J': {V(-1, 0), V(0, -1)},
        '7': {V(1, 0), V(0, -1)},
        'F': {V(1, 0), V(0, 1)},
        '.': set()}
    data = din.read().splitlines()
    fls, chunk = ''.join(data).index('S'), len(data[0])
    s = V(fls // chunk, fls % chunk)

    def moves(f, p):
        r = []
        for m in MOVES[data[f.x][f.y]]:
            d = V(f.x + m.x, f.y + m.y)
            dms = MOVES[data[d.x][d.y]]
            if V(-m.x, -m.y) in dms and d != p:
                r.append(d)
        return r

    cur, pcur, path, cnt = moves(s, None), [s, s], {s}, 1
    data[s.x] = data[s.x].replace('S', list(MOVES.keys())[
        list(MOVES.values()).index({
            V(cur[0].x - s.x, cur[0].y - s.y),
            V(cur[1].x - s.x, cur[1].y - s.y)})])
    path |= set(cur)
    while cur[0] != cur[1]:
        cnt += 1
        for i in (0, 1):
            pcur[i], cur[i] = cur[i], moves(cur[i], pcur[i])[0]
        path |= set(cur)

    def cross(rx, y):
        ns = [V(xi, y) in path and data[xi][y] or '.' for xi in rx]
        return sum([
            ns.count('-'), min(ns.count('F'), ns.count('J')),
            min(ns.count('7'), ns.count('L'))])

    nesteds = [
        V(x, y) not in path and cross(range(x), y) % 2
        for x in range(len(data)) for y in range(len(data[x]))]

    return cnt, sum(nesteds)

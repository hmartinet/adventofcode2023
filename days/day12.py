from functools import cache
from multiprocessing import Pool


@cache
def res(s, g, c=0):
    if not s:
        return not (c or g) or (c,) == g
    if g and c > g[0] or not g and c > 0:
        return 0
    return (
        (s[0] != '.' and res(s[1:], g, c + 1) or 0) +
        (s[0] != '#' and c == (g and g[0]) and res(s[1:], g[1:]) or 0) +
        (s[0] != '#' and c == 0 and res(s[1:], g) or 0))


def solve(din):
    a1, a2 = [], []
    for s, g in map(str.split, din.read().splitlines()):
        g = tuple(map(int, g.split(',')))
        a1.append((s, g))
        a2.append(('?'.join([s] * 5), g * 5))
    with Pool(10) as pool:
        r1 = sum(pool.starmap(res, a1))
        r2 = sum(pool.starmap(res, a2))
    return r1, r2

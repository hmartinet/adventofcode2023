from functools import cache
from multiprocessing import Pool


@cache
def d(a, b, e, z):
    a, b = sorted([a, b])
    return sum([e - 1 for c in z if a < c < b]) + b - a


def solve(din, e=1000000):
    data = [list(r) for r in din.read().splitlines()]
    g = tuple((x, y) for x, r in enumerate(data)
              for y, c in enumerate(r) if c == '#')
    z = tuple(tuple(c for c in range(len(data)) if c not in [g[i] for g in g])
              for i in (0, 1))

    def sumd(e):
        al = [(a[i], b[i], e, z[i]) for i, a in enumerate(g)
              for b in g[i:] for i in [0, 1]]
        with Pool(4) as pool:
            return sum(pool.starmap(d, al))

    return sumd(2), sumd(e)

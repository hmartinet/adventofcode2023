from heapq import heappop, heappush
from multiprocessing import Pool


def minheat(g, tx, ty, amin, amax):
    fs = list(range(1, amax + 1))
    q, cache = [(0, 0, 0, 1, 0), (0, 0, 0, 0, 1)], set()
    while q:
        heat, x, y, dx, dy = heappop(q)
        cv = (x, y, dx, dy)
        if cv in cache: continue
        cache.add(cv)
        if (x, y) == (tx, ty): return heat
        for dx, dy in ((dy, dx), (-dy, -dx)):
            px, py, h = x, y, heat
            for i in fs:
                px, py = px + dx, py + dy
                if not (0 <= px <= tx and 0 <= py <= ty): continue
                h += g[px][py]
                if i < amin: continue
                heappush(q, (h, px, py, dx, dy))


def solve(din):
    g = [list(map(int, r)) for r in din.read().splitlines()]
    tx, ty = len(g) - 1, len(g[0]) - 1
    with Pool(2) as pool:
        return tuple(pool.starmap(minheat, [
            (g, tx, ty, 1, 3), (g, tx, ty, 4, 10)]))

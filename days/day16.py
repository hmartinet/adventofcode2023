
from multiprocessing import Pool


def energized(g, gl, *m):
    np = lambda px, py, dx, dy: (px + dx, py + dy, dx, dy)

    q, moves, path = [(m)], set(), set()
    for m in q:
        px, py, dx, dy = m
        if m in moves or not (0 <= px < gl and 0 <= py < gl):
            continue
        moves.add(m)
        path.add(px + py * gl)
        s = g[px][py]
        if s == '.' or (not dy and s == '|') or (not dx and s == '-'):
            q.append(np(*m))
        elif s == '/':
            q.append(np(px, py, -dy, -dx))
        elif s == '\\':
            q.append(np(px, py, dy, dx))
        elif s == '|':
            q.extend([np(px, py, 1, 0), np(px, py, -1, 0)])
        elif s == '-':
            q.extend([np(px, py, 0, 1), np(px, py, 0, -1)])
    return len(path)


def solve(din):
    g = din.read().splitlines()
    gl = len(g)

    r1 = energized(g, gl, 0, 0, 0, 1)
    a = [[(g, gl, c, 0, 0, 1), (g, gl, c, gl - 1, 0, -1),
          (g, gl, 0, c, 1, 0), (g, gl, gl - 1, c, -1, 0)] for c in range(gl)]
    with Pool(10) as pool:
        r2 = max(pool.starmap(energized, sum(a, [])))
    return r1, r2

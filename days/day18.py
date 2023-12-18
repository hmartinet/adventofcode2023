DN = [(1, 0), (0, 1), (-1, 0), (0, -1)]
DD = dict(zip(['R', 'D', 'L', 'U'], DN))


def solve(din):
    parse = lambda d1, n1, c: (d1, int(n1), int(c[7]), int(c[2:7], 16))
    shift = lambda px, py, dx, dy, n: ((px, py), (px + dx * n, py + dy * n))
    cross = lambda lx, ly, rx, ry: (lx * ry - ly * rx)

    r1, r2, a1, a2 = (0, 0), (0, 0), 0, 0
    for r in din.read().splitlines():
        d1, n1, d2, n2 = parse(*r.split())
        l1, r1 = shift(*r1, *DD[d1], n1)
        l2, r2 = shift(*r2, *DN[d2], n2)
        a1 += cross(*l1, *r1) + n1
        a2 += cross(*l2, *r2) + n2
    return a1 // 2 + 1, a2 // 2 + 1

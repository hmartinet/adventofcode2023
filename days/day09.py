from functools import reduce


def solve(din):
    data = [[[int(n) for n in l.split()]] for l in din.readlines()]

    rl = [0, 0]
    for l in data:
        while sum(l[-1]) != 0:
            l.append(reduce(
                lambda r, b: (b, r[1] + [b - r[0]]),
                l[-1][1:], (l[-1][0], []))[1])
        rl[0] += reduce(lambda r, s: r + s[-1], l[::-1], 0)
        rl[1] += reduce(lambda r, s: s[0] - r, l[::-1], 0)

    return tuple(rl)

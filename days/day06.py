from math import ceil, floor, prod, sqrt


def solve(din):
    lines = din.readlines()
    runs = list(zip(*[map(int, l.split()[1:]) for l in lines]))
    t2, d2 = [int(''.join(l.split()[1:])) for l in lines]

    def f(t, d):
        dt = sqrt(t * t - 4 * d)
        return ceil((t + dt) / 2) - floor((t - dt) / 2) - 1

    return prod([f(t, d) for t, d in runs]), f(t2, d2)

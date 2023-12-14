from hashlib import sha1

turn = lambda r: list(zip(*r[::-1]))
roll = lambda r: list(map(lambda c: [
    *'#'.join([r.ljust(len(g), '.') for r, g in zip(
        ''.join(c).replace('.', '').split('#'),
        ''.join(c).split('#'))])], r))
weight = lambda r: sum(map(
    lambda e: e[1] == 'O' and e[0], enumerate(r[::-1], 1)))


def solve(din):
    rocks = turn(turn(turn(din.read().splitlines())))
    r1 = sum(map(weight, roll(rocks)))

    i, nf, cache = 0, 1, []
    while i < 1000000000:
        for __ in range(4):
            rocks = turn(roll(rocks))
        if nf:
            h = sha1(repr(rocks).encode()).digest()
            if h in cache:
                c = i - cache.index(h)
                i, nf = ((1000000000 - i) // c) * c + i, 0
            cache.append(h)
        i += 1
    r2 = sum(map(weight, rocks))

    return r1, r2

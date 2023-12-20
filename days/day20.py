import re
from collections import defaultdict, deque
from math import lcm
from operator import mul

RP = re.compile(r"([&%]?)(\S+) -> (.+)")


def solve(din):
    S, SC, F, C, N = defaultdict(bool), defaultdict(list), set(), set(), {}
    for o, k, s in map(lambda l: RP.match(l).groups(), din.readlines()):
        N[k] = s.split(", ")
        {'%': F, '&': C}.get(o, set()).add(k)
        for n in N[k]: SC[n].append(k)

    r1 = [0, 0]
    for _ in range(1000):
        r1[0] += 1
        q = deque([(n, 0) for n in N["broadcaster"]])
        while q:
            k, v = q.pop()
            r1[v] += 1
            if k in F:
                if v: continue
                S[k] ^= 1
            elif k in C: S[k] = not all(S[c] for c in SC[k])
            for n in N.get(k, []):
                q.appendleft((n, S[k]))

    r2 = []
    for k in N['broadcaster']:
        bn = ''
        while k:
            bn += '01'[any(set(N[k]) & C)]
            k, = set(N[k]) & F or [0]
        r2.append(int(bn[::-1], 2))

    return mul(*r1), lcm(*r2)

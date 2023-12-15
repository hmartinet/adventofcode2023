from collections import OrderedDict as odict
from functools import cache

from tools import cmap

h = cache(lambda s: cmap(s, lambda r, c: ((r + ord(c)) * 17) % 256))


def solve(din):
    def op(s):
        sl = lambda b, l: b.setdefault(h(l) + 1, odict())
        return [lambda: lambda b: sl(b, s[:-2]).update({s[:-2]: int(s[-1:])}),
                lambda: lambda b: sl(b, s[:-1]).pop(s[:-1], None)]['-' in s]()

    seq, b = din.read().strip().split(','), {}
    [o(b) for o in map(op, seq)]
    return sum(map(h, seq)), sum([
        i * k * v[1] for i in sorted(b.keys())
        for k, v in enumerate(b[i].items(), 1)])

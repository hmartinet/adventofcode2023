from collections import OrderedDict
from functools import cache


@cache
def hash(s, r=0):
    for c in s:
        r = ((r + ord(c)) * 17) % 256
    return r


def solve(din):
    def oper(s):
        sl = lambda b, l: b.setdefault(hash(l), OrderedDict())
        return [lambda: lambda b: sl(b, s[:-2]).update({s[:-2]: int(s[-1:])}),
                lambda: lambda b: sl(b, s[:-1]).pop(s[:-1], None)]['-' in s]()

    seq = din.read().strip().split(',')
    r1, r2 = sum(map(hash, seq)), 0
    boxes = {}; [op(boxes) for op in map(oper, seq)]
    for i in sorted(boxes.keys()):
        for k, v in enumerate(boxes[i].items()):
            r2 += (i + 1) * (k + 1) * v[1]
    return r1, r2

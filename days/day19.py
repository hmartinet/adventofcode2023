import re
from copy import deepcopy
from functools import reduce
from json import loads
from operator import mul

RWF = re.compile(r'(\w+)\{(.*)\}')
RRU = re.compile(r'(\w+)(<|>)(\d+):(\w+)')
RRA = lambda s: re.sub(r'(\w)=(\d+)', r'"\1":\2', s)
OP1 = {'<': lambda v: lambda x: x < v, '>': lambda v: lambda x: x > v}
OP2 = {'<': lambda v: lambda l, r: (r < v and ([l, r], None)) or
       (l < v and ([l, v - 1], [v, r])) or (None, [l, r]),
       '>': lambda v: lambda l, r: (l > v and ([l, r], None)) or
       (r > v and ([v + 1, r], [l, v])) or (None, [l, r])}


def solve(din):
    def p1(ratings):
        for w, ra in ratings:
            while True:
                rus, ow = wfs[w]
                for c, f, _, w in rus:
                    if f(ra[c]): break
                else: w = ow
                if w == 'A': yield sum(ra.values())
                elif w != 'R': continue
                break

    def p2(w, ra):
        rus, ow = wfs[w]
        for c, _, f, w in rus:
            tr, fr = f(*ra[c])
            if tr:
                tra = deepcopy(ra); tra[c] = tr
                if w == 'A': yield tra
                elif w != 'R': yield from p2(w, tra)
            if not fr: return
            ra[c] = fr
        else: w = ow
        if w == 'A': yield ra
        elif w != 'R': yield from p2(w, ra)

    win, rin = din.read().split('\n\n'); wfs = {}
    for wf in win.splitlines():
        name, rs = RWF.match(wf).groups(); rs = rs.split(',')
        rules = [(c, OP1[op](int(v)), OP2[op](int(v)), w) for c, op, v, w in [
            RRU.match(r).groups() for r in rs[:-1]]]
        wfs[name] = (rules, rs[-1])

    return (
        sum(p1([('in', loads(r)) for r in RRA(rin).splitlines()])),
        sum([reduce(mul, ((r - l + 1) for l, r in rd.values()), 1)
             for rd in p2('in', {r: [1, 4000] for r in 'xmas'})]))

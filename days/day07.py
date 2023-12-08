#!/usr/bin/env python3

from collections import Counter


def solve(din):
    cards1 = '23456789TJQKA'
    cards2 = 'J23456789TQKA'
    types = [
        (1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 2, 2),
        (1, 1, 3), (2, 3), (1, 4), (5,)]

    def joker_type(h):
        return max([types.index(tuple(sorted(Counter(
            h.replace('J', c)).values()))) for c in cards2])

    hands = [l.split() for l in din.readlines()]
    hands1 = sorted(hands, key=lambda h: (
        types.index(tuple(sorted(Counter(h[0]).values()))),
        tuple(cards1.index(c) for c in h[0])))
    hands2 = sorted(hands, key=lambda h: (
        joker_type(h[0]),
        tuple(cards2.index(c) for c in h[0])))

    return (
        sum([(n + 1) * int(h[1]) for n, h in enumerate(hands1)]),
        sum([(n + 1) * int(h[1]) for n, h in enumerate(hands2)]))

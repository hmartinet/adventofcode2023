from math import pow


def solve(din):
    lines = din.readlines()
    cards, hand = [], [1] * len(lines)
    for i, l in enumerate(lines):
        wn, mn = map(str.split, l.split('|'))
        r = len(set(wn) & set(mn))
        cards.append(r)
        for j in range(i + 1, i + 1 + r):
            hand[j] += hand[i]

    return (
        sum([int(pow(2, c - 1)) for c in cards]),
        sum(hand))

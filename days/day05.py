from functools import reduce


def solve(din):
    seeds, *maps = din.read().strip().split('\n\n')
    seeds = list(map(int, seeds.split()[1:]))

    def lookup(inputs, m):
        for start, length in inputs:
            while length > 0:
                for mv in m.split('\n')[1:]:
                    dst, src, l = map(int, mv.split())
                    delta = start - src
                    if delta in range(l):
                        l = min(l - delta, length)
                        yield (dst + delta, l)
                        start += l
                        length -= l
                        break
                else:
                    yield (start, length)
                    break

    return tuple([min(reduce(lookup, maps, s))[0] for s in [
        zip(seeds, [1] * len(seeds)),
        zip(seeds[0::2], seeds[1::2])]])

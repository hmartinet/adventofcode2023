

def sym(g, mis=0):
    for i in range(1, len(g)):
        if sum([l != r for lr, rr in zip(g[:i][::-1], g[i:])
                for l, r in zip(lr, rr)]) == mis:
            return i
    return 0


def solve(din):
    blocks, r1, r2 = din.read().split("\n\n"), 0, 0
    for block in blocks:
        grid = block.splitlines()
        r1 += 100 * sym(grid) + sym(list(zip(*grid)))
        r2 += 100 * sym(grid, 1) + sym(list(zip(*grid)), 1)
    return r1, r2

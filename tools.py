def cmap(it, f, r=0):
    for e in it:
        r = f(r, e)
    return r

from sys import argv
from itertools import product

fs = lambda *e: frozenset(e)

def prefixes(a):
    return frozenset(a[:d+1] for d in range(len(a)))

def suffixes(a):
    return frozenset(a[d:] for d in range(len(a)))

assert prefixes('abc') == fs('a', 'ab', 'abc')
assert suffixes('abc') == fs('c', 'bc', 'abc')

words = frozenset(argv[1:])

def coding(w):
    for l, r in product(w, repeat=2):
        base = w - fs(l, r)
        for ovl in suffixes(l) & prefixes(r):
            if ovl == l == r:
                continue
            if ovl == l:
                return coding(base | fs(l, r[len(ovl):]))
            if ovl == r:
                return coding(base | fs(r, l[:-len(ovl)]))
            return coding(base | fs(ovl, r[len(ovl):], l[:-len(ovl)]))
    return w

print(coding(words))

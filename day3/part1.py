#!/usr/bin/env python3

def parseinput(f):
    with open(f) as fh:
        return [ x.strip('\n') for x in fh.readlines() ]

import string
def priorities():
    v = 1
    worth = {}
    for c in string.ascii_lowercase + string.ascii_uppercase:
        worth[c] = v
        v+=1
    return worth


def firstsecond(contents):
    l = int(len(contents) / 2)
    return set(c for c in contents[:l]), set(c for c in contents[l:])

def both(a, b):
    return a.intersection(b)

def go(alist):
    w = priorities()

    count = 0
    for e in alist:
        f, s = firstsecond(e)
        for dup in both(f, s):
            count += w[dup]
    print("total sum of duplicates: ", count)

if __name__ == "__main__":
    go(parseinput('input.txt'))

#!/usr/bin/env python3
import itertools

def grouper(iterable, n):
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args)

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

def bag(contents):
    l = int(len(contents) / 2)
    return set(c for c in contents)

def both(a, b):
    return a.intersection(b)

def three(a, b, c):
    return a.intersection(b).intersection(c)

def go(alist):
    w = priorities()

    count = 0
    for elvegroup in grouper(alist, 3):
        a, b, c = bag(elvegroup[0]), bag(elvegroup[1]), bag(elvegroup[2])
        o = three(a, b, c) # overlap between 3 bags
        count+=w[o.pop()]
    print("sum of priorities", count)

if __name__ == "__main__":
    go(parseinput('input.txt'))

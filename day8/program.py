#!/usr/bin/python3
from time import time
def timed_function(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        r = func(*args, **kwargs)
        t2 = time()
        print(f'F {func.__name__!r} took {(t2 - t1):.4f}s')
        return r

    return wrapper

import numpy as np
def parseinput(filepath):
    with open(filepath) as fh:
        l = [[int(y) for y in x.strip('\n')]
                for x in fh.readlines()]
    return np.array(l)

@timed_function
def day8a(filepath):
    g = parseinput(filepath)

    # visible
    v = np.zeros_like(g)
    v[0] = v[-1] = v[:,0] = v[:,-1] = 1; 

    for row in range(1, g.shape[0]-1): # row
        for col in range(1, g.shape[1]-1): # col
            me = g[row][col]
            if g[:,col][:row].max() < me: # north
                v[row][col] = 1
            elif g[:,col][row+1:].max() < me: # south
                v[row][col] = 1
            elif g[row][:col].max() < me: # west
                v[row][col] = 1
            elif g[row][col+1:].max() < me: # east
                v[row][col] = 1

    return v.shape[0]*v.shape[1] - v[v == 0].size

def countwhile(iterable, value):
    c=0
    for x in iterable:
        if x < value:
            c+=1
        else: # first higher tree
            c+=1
            break
    return c

@timed_function
def day8b(filepath):
    g = parseinput(filepath)
    v = np.zeros_like(g)

    for row in range(g.shape[0]): # row
        for col in range(g.shape[1]): # col
            me = g[row][col]

            n = countwhile(np.flip(g[:,col][:row]), me)
            s = countwhile(g[:,col][row+1:], me)
            w = countwhile(np.flip(g[row][:col]), me)
            e = countwhile(g[row][col+1:], me)
            v[row][col] = n*s*w*e

    return v.max()

def main():
    assert day8a('example.txt') == 21
    print(f"Part 1: {day8a('input.txt')}")

    assert day8b('example.txt') == 8
    print(f"Part 2: {day8b('input.txt')}")

if __name__ == "__main__": main()


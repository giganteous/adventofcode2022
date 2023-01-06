#!/usr/bin/python3
import itertools
from time import time
def timed_function(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        r = func(*args, **kwargs)
        t2 = time()
        print(f'F {func.__name__!r} took {(t2 - t1):.4f}s')
        return r

    return wrapper

def read(f):
    with open(f) as fh:
        return [ x.strip('\n') for x in fh.readlines() ]

def key(a, b): return tuple(sorted([a, b]))

import re
def parse(f):
    lines = read(f)
    r = re.compile('^Valve (?P<source>[A-Z]+) has flow rate=(?P<rate>[0-9]+); tunnels? leads? to valves? (?P<leads>[A-Z, ]+)$')
    m = {}
    for line in lines:
        g = r.match(line)
        source, rate, leads = g.groups()
        d = g.groupdict()
        if ',' in leads:
            leads = leads.split(', ')
        else:
            leads = [leads]
        m[source] = { 'rate': int(rate), 'leads': leads }

    poi = [k for k, v in m.items() if v['rate'] > 0]
    return m, poi

def leads(valves, source):
    for lead in valves[source]['leads']:
        yield lead

from heapq import heappush, heappop
def shortestpath(valves, s, end):
    todo = [(0, s)]
    visited = set()
    costs = {}

    while todo:
        cost, node = heappop(todo)
        if node == end:
            return cost
        for l in leads(valves, node):
            if l in visited:
                continue

            if cost + 1 < costs.get(l, float('inf')):
                costs[l] = cost + 1
                heappush(todo, (cost + 1, l))

        visited.add(node)

@timed_function
def map_travelcosts(valves, poi):
    tc = {}
    for p in poi:
        tc[key('AA', p)] = shortestpath(valves, 'AA', p)

    # then from each point to other points
    for s, e in itertools.combinations(poi, 2):
        tc[key(s, e)] = shortestpath(valves, s, e)
    return tc


from collections import namedtuple
from dataclasses import dataclass

Qitem = namedtuple('qitem', ('pri', 'path', 'closed', 't_rem', 'flow', 'flowtot'))

@timed_function
def day16a(filepath):
    # valve-map, points of interest
    valves, poi = parse(filepath)

    T = map_travelcosts(valves, poi)
    R = {x: valves[x]['rate'] for x in poi}

    todo = [Qitem(0, ('AA',), frozenset(poi), 30, 0, 0)]
    best = 0

    positions = []
    while todo:
        pri, path, closed, t_rem, flow, flowtot = heappop(todo)
        depth = len(path)
        if depth == 2 or (depth == 3 and path[:2] == ('AA', 'IY')):
            print(f'trying {path}')

        if t_rem == 0: # t_rem
            if flowtot > best:
                print(f'amount reachable:\n{flowtot} via {path}')
                best = flowtot
            continue

        # filter out unreachable valves
        possible = [y for y in closed if T[key(path[-1],y)]+1 < t_rem]
        if not len(possible):
            end = flowtot + (t_rem*flow)
            if end > best:
                print(f'cannot move; remaining {t_rem}, flow={flow}, flowtot={flowtot}')
                print(f'amount reachable:\n{end} via {path}')
                best = end
            continue

        # sort best options:
        sort = lambda x: -(t_rem - 1 - T[key(path[-1],x)])
        for v in sorted(possible, key=sort):
            oc = 1 + T[key(path[-1],v)]
            q = Qitem(
                -(t_rem - oc),
                (*path, v),    # path
                closed.difference({v}),            # new closed
                t_rem - oc,    # t_remaining
                flow + R[v], # new flow
                flowtot + (oc*flow) # total flow
                )
            if depth == 1:
                print(f"queueing {q}")
            heappush(todo, q)

    return best

if __name__ == "__main__":
    #ret = day16a('example.txt')
    #assert(ret == 1651)
    #print(f'Example: {ret}')

    print('#correct: IY,XF,IU,JF,JG,QH,SZ,BF')
    ret = day16a('input.txt')
    #assert(ret == 1947)
    print(f'Part1: {ret}')

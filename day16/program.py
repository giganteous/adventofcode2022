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


@timed_function
def day16a(filepath):
    # valve-map, points of interest
    valves, poi = parse(filepath)

    tc_map = map_travelcosts(valves, poi)
    rate_map = {x: valves[x]['rate'] for x in poi}

    # write recursive function to map estimations
    def map_estimations(path, t_rem, closed):
        gain = t_rem * rate_map.get(path[-1], 0)

        maxGain = gain
        maxChoice = path
        for c in closed:
            open_cost = tc_map[key(path[-1], c)] + 1
            if open_cost >= t_rem:
                continue
            gain, choice = map_estimations((*path, c), t_rem - open_cost, closed.difference({c}))
            if gain > maxGain:
                maxGain = gain
                maxChoice = (*path, c)
                
        return maxGain, maxChoice

    max, path = map_estimations(('AA',), 30, frozenset(poi))
    print(path)
    return max

if __name__ == "__main__":
    ret = day16a('example.txt')
    #assert(ret == 1651)
    print(f'Example: {ret}')

    ret = day16a('input.txt')
    print(f'Part1: {ret[0]}')

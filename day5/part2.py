#!/usr/bin/env python3

def read(f):
    with open(f) as fh:
        return [x.strip('\n') for x in fh.readlines()]

def parse(lines):
    header = ''
    stacks = []
    commands = []
    for n in range(0, len(lines)):
        if lines[n] == '':
            header = lines[n-1]
            stacks = lines[:n-1]
            commands = lines[n+1:]
            break
    # process stack
    stacks.reverse()
    # process header
    header = int(header.strip()[-1:])
    return header, stacks, commands

def positions(mx=3):
    return list(zip(range(0, mx), range(1, mx*4, 4)))

def makestacks(lines, width=3):
    matrix = [[] for i in range(width)]
    each = positions(width)
    if len(matrix) != len(each):
        raise

    for line in lines:
        print("processing ", line)
        for idx, e in each:
            v = line[e]
            if v != ' ':
                #print("-> matrix[{0}].append({1})".format(idx, v))
                matrix[idx].append(v)
    return matrix

def move(matrix, count, source, dest):
    values = []
    for i in range(count):
        values.append(matrix[source - 1].pop())
    values.reverse()
    #print("-> moving {0} crates from {1} to {2}".format(values, source, dest))
    matrix[dest - 1].extend(values)

import re, sys
file = 'example.txt'
if len(sys.argv) > 1:
    file = sys.argv[1]
l = read(file)
h, s, c = parse(l)
matrix = makestacks(s, width=h)

commands = []
r = re.compile('move (?P<count>[0-9]+) from (?P<source>[0-9]+) to (?P<dest>[0-9]+)')
for line in c:
    g = r.match(line)
    commands.append([int(x) for x in g.groups()])

for element in commands:
    move(matrix, *element)

for idx in range(len(matrix)):
    print("top item in row {0} is {1}".format(idx, matrix[idx][-1:]))


#!/usr/bin/env python3

def read(p):
    with open(p, 'r') as fh:
        return [x.strip('\n') for x in fh.readlines()]

class buffer():
    value = ''
    window = 4

    def __init__(self, value, window=4):
        print('B:', value, ' (window =', window, ')')
        self.value = value
        self.window = window

    def movewhile(self):
        pos = self.window
        while len(set(self.value[pos-self.window:pos])) < self.window:
            pos+=1
        return pos

def example(v):
    b = buffer(v)
    while b.test():
        print('moved to ', b.start)

    print('start is now at ', b.start,', end of marker is at ', b.start + 4)

#b = buffer('mjqjpqmgbljsphdztnvjfqwrcgsmlb')
#print(b.movewhile())
assert(buffer('mjqjpqmgbljsphdztnvjfqwrcgsmlb').movewhile() == 7)
assert(buffer('bvwbjplbgvbhsrlpgdmjqwftvncz').movewhile() == 5)
assert(buffer('nppdvjthqldpwncqszvftbrmjlhg').movewhile() == 6)
assert(buffer('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg').movewhile() == 10)
assert(buffer('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw').movewhile() == 11)

import sys
if len(sys.argv) > 1:
    fh = open(sys.argv[1])
    value = fh.read().strip('\n')
    print('in file {0}, position would be {1}'.format(sys.argv[1], buffer(value).movewhile()))


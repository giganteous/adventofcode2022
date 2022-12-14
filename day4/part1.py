#!/usr/bin/env python3

def read(f):
    with open(f) as fh:
        return [x.strip('\n') for x in fh.readlines()]

class assignment():
    s = set()
    start = 0
    end = 0

    def __init__(self, start, stop):
        start, stop = int(start), int(stop)
        self.s = set(range(start, stop+1))
        self.start = start
        self.stop = stop
    def __str__(self):
        return '........   {0}-{1}'.format(self.start, self.stop)
    def __len__(self):
        return len(self.s)
    def intersection(self, other):
        if type(self) != type(other):
            raise TypeError
        return self.s.intersection(other.s)

def fullycontains(s1, s2):
    smallest = min(len(s1), len(s2))
    return len(s1.intersection(s2)) >= smallest

def go(alist):
    paircount = 0
    for pair in alist:
        left, right = [ f.split('-') for f in pair.split(',') ]
        #print(left, right)
        b1, b2 = assignment(left[0], left[1]), assignment(right[0], right[1])
        if fullycontains(b1, b2):
            paircount += 1
            #print(b1)
            #print(b2)
            #print(" one overlaps fully with other")
    print("total overlap count: ", paircount)
            
if __name__ == "__main__":
    go(read('input.txt'))

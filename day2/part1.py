#!/usr/bin/env python3

import sys

def readfile(p):
    with open(p, 'r') as f:
        return [x.strip('\n').split(' ') for x in f.readlines()]

class paper():
    def value(self):
        return 2
    def score(self, other):
        if isinstance(other, rock):
            return 6 + self.value()
        elif isinstance(other, scissor):
            return 0 + self.value()
        return 3 + self.value()

class rock():
    def value(self):
        return 1
    def score(self, other):
        if isinstance(other, scissor):
            return 6 + self.value()
        elif isinstance(other, paper):
            return 0 + self.value()
        return 3 + self.value()

class scissor():
    def value(self):
        return 3
    def score(self, other):
        if isinstance(other, paper):
            return 6 + self.value()
        elif isinstance(other, rock):
            return 0 + self.value()
        return 3 + self.value()

mapping = {
        'A': rock(),
        'B': paper(),
        'C': scissor(),
        'X': rock(),
        'Y': paper(),
        'Z': scissor(),
        }

def process():
    rounds = readfile('input.txt')
    total = 0
    for r in rounds:
        opponent, you = mapping[r[0]], mapping[r[1]]
        #print((opponent, you))
        #print('playing other ', opponent, ' against me ', you)
        total += you.score(opponent)
    print('the final total is ', total)

if __name__ == "__main__":
    process()


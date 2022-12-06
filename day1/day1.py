#!/usr/bin/env python3

import sys

def readfile(p):
    with open(p, 'r') as f:
        return [x.strip('\n') for x in f.readlines()]

def process():
    elve = 1
    total = []
    thiselve = []
    highest = 0
    highestelve = 1
    for entry in readfile('input.txt'):
        if entry == '':
            total.append({'elve': str(elve), 'food': thiselve.copy(), 'total': sum(thiselve)})
            if sum(thiselve) > highest:
                highest = sum(thiselve)
                highestelve = elve
            thiselve = []
            elve += 1
        else:
            thiselve.append(int(entry))

    print('highest elve is ', highestelve, ' with total food ', highest)
    return total

if __name__ == "__main__":
    data = process()
    top3 = sorted(data, key=lambda elve: sum(elve['food']))[-3:]
    print('highest elve is ', top3[2]['elve'], ' with total food ', sum(top3[2]['food']))
    total = 0
    for x in top3:
        total = total + sum(x['food'])
    print('sum of top3 elves is ', total)



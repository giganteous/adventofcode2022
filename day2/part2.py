#!/usr/bin/env python3

def readfile(p):
    with open(p, 'r') as f:
        return [x.strip('\n') for x in f.readlines()]

# A: Rock, worth 1
# B: Paper, worth 2
# C: Scissors, worth 3
# Win: 6
# draw: 3
# loss: 0
mapping = {
        'A X': 3 + 0, # i loose, choose c
        'A Y': 1 + 3, # draw, choose a
        'A Z': 2 + 6, # i win, choose b 
        'B X': 1 + 0, # i loose, choose a
        'B Y': 2 + 3, # draw, choose b
        'B Z': 3 + 6, # i win, choose c 
        'C X': 2 + 0, # i loose, choose c
        'C Y': 3 + 3, # draw, choose a
        'C Z': 1 + 6, # i win, choose b 
        }

def process():
    rounds = readfile('input.txt')
    total = 0
    for r in rounds:
        total += mapping[r]
    print('the final total is ', total)

if __name__ == "__main__":
    process()

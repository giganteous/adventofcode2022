#!/usr/bin/python3
import itertools
from dataclasses import dataclass
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

@timed_function
def day10a(filepath):
    lines = read(filepath)

    cycle = 1
    processing = None
    alarmqueue = enumerate(range(20, 221, 40))
    alarm = next(alarmqueue)
    register = 1
    s = 0
    while True:
        if cycle == alarm[1]:
            s += (cycle * register)
            print(f'[alarm] {cycle}: {register} ({cycle*register}, tot={s})')
            try:
                alarm = next(alarmqueue)
            except:
                print('alarmqueue is empty')
                break

        if not processing:
            if len(lines) == 0: break
            command = lines.pop(0)
            match command.split():
                case ("addx", amount):
                    #print(f'next command, addx {amount}')
                    processing = (2, int(amount))
                case ("noop",):
                    #print(f'next command, noop')
                    processing = (1, 0)
                case other:
                    #print(f"Illegal command: {other}")
                    raise

        c, howmuch = processing
        c -= 1
        if c == 0:
            register += howmuch
            processing = None
        else:
            processing = (c, howmuch)
        cycle += 1
        continue

        cycle += 1
    return s

@timed_function
def day10b(filepath):
    lines = enumerate(read(filepath))

    cycle = 0
    processing = None
    register = 1
    screen = [' '] * 240
    def pixelate(cycle, register):
        test = cycle % 40
        if test-1 in (register, register-1, register+1):
            p = '#'
        else:
            p = '.'
        try:
            screen[cycle-1] = p
        except IndexError:
            print('INDEX ERROR: x was ', cycle, 'value', p)
    def spritepos(x):
        s = ['.'] * 40
        s[x] = s[x-1] = s[x+1] = '#'
        #print('Sprite position:', ''.join(s))
    def allrows():
        for start, stop in zip(range(0, 201, 40), range(40, 241, 40)):
            print('Current CRT row:', ''.join(screen[start:stop]))

    def crtrow(x):
        for start, stop in zip(range(0, 201, 40), range(40, 241, 40)):
            if x > start and x <= stop:
                print('Current CRT row:', ''.join(screen[start:stop]))

    #spritepos(register)
    row, command = 0, '---'
    while True:
        cycle += 1
        #print()

        if not processing:
            try:
                row, command = next(lines)
            except:
                break

            match command.split():
                case ("addx", amount):
                    processing = (2, int(amount))
                case ("noop",):
                    processing = (1, 0)
                case other:
                    raise
            #print(f'Start cycle {cycle}: begin executing {row}: {command}')

        #print(f'During cycle {cycle}: CRT draws pixel in position {cycle-1} (X={register})')
        pixelate(cycle, register)

        #crtrow(cycle)

        c, howmuch = processing
        c -= 1
        if c == 0: # move sprite
            register += howmuch
            #print(f'End of cycle {cycle}: finish executing {row}: {command} (Register X is now {register}')
            #spritepos(register)
            processing = None
        else:
            processing = (c, howmuch)
    allrows()

#day10a('small.txt')
if __name__ == '__main__':
    #assert(day10a('example.txt') == 13140)
    #day10b('example.txt')
    day10b('input.txt')

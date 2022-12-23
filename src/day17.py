#!/bin/env python3 
from itertools import cycle
from collections import deque

def draw(rocks):
    h = max([y for _, y in rocks])
    for y in range(h, 0, -1):
        row = ''
        for x in range(7):
            if (x,y) in rocks:
                row += '#'
            else:
                row += '.'
        print("".join(row))

shifts = cycle(open('inputs/day17').readlines()[0].strip())
shapes = cycle(['-', '+', 'L', '|', 'x'])

width = 7
rocks = set([(i,0) for i in range(width)])
h = 0 

"""
How could you tell if it's repeating?
After how many rocks is shifts and shapes in phase again?
No, because the rocks below doesn't have to be "#######"

So the shift and shape should be in sync and the context below should be
the same as last time it happend.

So I need to hash the shift, shape and rocks below.
"""

def hash(shape, shift, row):
    byte = 0

    # msb
    h = min([y if y is not None else 0 for y in row])
    for i in range(width):
        if row[i] is not None:
            x = row[i] - h
            byte |= x
            byte <<= 2

    # then comes the shape
    byte <<= 3
    match shape:
        case '-': byte |= 0b000
        case '+': byte |= 0b001
        case 'L': byte |= 0b010
        case '|': byte |= 0b011
        case 'x': byte |= 0b100

    # lsb
    byte <<= 1
    if shift == '>': byte |= 1

    return byte

def unhash(byte):
    assert(not (byte & (1 << 19)))

    shift = byte & 1
    byte >>= 1

    shape = byte & 0b111
    byte >>= 3

    top = ''
    for i in range(width):
        if byte & (1 << i):
            top = '#' + top
        else:
            top = '.' + top

    return shape, shift, top, n

tops = set()
topsn = {}

nshifts = len(open('inputs/day17').readlines()[0].strip())
repeat = False
n = 0
nr = 0
# for _ in range(114):
while not repeat or (repeat and nr > 0):
    h = h + 4
    shape = next(shapes)
    match shape:
        case '-':
            top = deque([None, None, h, h, h, h, None])
            rock = set([(2, h), (3, h), (4, h), (5,h)])
        case '+':
            top = deque([None, None, h+1, h+2, h+1, None, None])
            rock = set([(2,h+1), (3,h+1), (4,h+1), (3,h), (3,h+2)])
        case 'L':
            top = deque([None, None, h, h, h+2, None, None])
            rock = set([(2, h), (3, h), (4,h), (4,h+1), (4,h+2)])
        case '|':
            top = deque([None, None, h+3, None, None, None, None])
            rock = set([(2,h),(2,h+1), (2,h+2),(2,h+3)])
        case 'x':
            top = deque([None, None, h+1, h+1, None, None, None])
            rock = set([(2,h), (3,h), (2,h+1),(3,h+1)])

    falling = True
    while falling:
        shift = next(shifts)
        match shift:
            case '<':
                if not any(x == 0 for x, _ in rock):
                    rock = set([(x-1,y) for x,y, in rock])
                    if rock & rocks:
                        rock = set([(x+1,y) for x,y, in rock])
                    else:
                        top.rotate(-1)
            case '>':
                if not any(x == 6 for x, _ in rock):
                    rock = set([(x+1,y) for x,y, in rock])
                    if rock & rocks:
                        rock = set([(x-1,y) for x,y, in rock])
                    else:
                        top.rotate(1)
       
        rock = set([(x, y-1) for x,y in rock])
        if rock & rocks:
            rock = set([(x,y+1) for x,y in rock])
            rocks |= rock
            h = max([y for _, y in rocks])
            top = hash(shape, shift, top)
            if top in tops and not repeat:
                rtop = top
                nr = n
                hr = h
                repeat = True
                break
            tops.add(top)
            topsn[top] = n
            falling = False
        if repeat:
            nr -= 1
    n += 1

rocks = [(x,y-hr) for x,y in rocks if y > hr]
draw(rocks)
print(n, topsn[rtop])

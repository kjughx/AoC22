#!/bin/env python3

import numpy as np

def walk(steps, vec, start, cur, end):
    s = cur
    vec[s] = 'v'
    l = end - start
    for _ in range(steps):
        ns = (s + 1) % l
        if vec[ns] != '#' and vec[ns] != ' ':
            vec[ns] = 'v'
            s = ns

    # vec[s] = 'v'
    # for _ in range(steps):
    #     if vec[(s+1)%len(vec)] != '#' and vec[(s+1)%len(vec)] != ' ':
    #         vec[s] = 'v'
    #         s = ((s + 1) % len(vec))
    # vec[s] = 'x'
    # return s, vec

def rotate(dir, cur):
    match dir,cur:
        case ['R', 'R']: return 'D'
        case ['R', 'L']: return 'U'
        case ['D', 'R']: return 'L'
        case ['D', 'L']: return 'R'
        case ['L', 'R']: return 'U'
        case ['L', 'L']: return 'D'
        case ['U', 'R']: return 'R'
        case ['U', 'L']: return 'L'

with open('inputs/day22') as file:
    lines = [line.strip('\n') for line in file.readlines()]
    ipath = iter(lines[-1])

    c = next(ipath)
    path = []
    op = ''
    try:
        while True:
            if c == 'R' or c == 'L':
                path.append(int(op))
                path.append(c)
                c = next(ipath)
                op = ''
                continue

            op += c
            c = next(ipath)
    except:
        pass

    grid = np.array(lines[:-2])
    maxl = max([len(row) for row in grid])
    for i, row in enumerate(grid):
        grid[i] += ' '*(maxl-len(row))

    grid = np.array([str(c) for line in grid for c in line]).reshape((len(lines[:-2]), maxl))

    # grid[:, 0]  : col 0
    # grid[0, :]  : row 0
    mc = len(grid[:, 0])
    mr = len(grid[0])

    rstart = {i: list(row).index('.') for i, row in enumerate(grid)}
    rend = {i: mr - list(reversed(row)).index('.') + 1 for i, row in enumerate(grid)}
    rsize = {i: (rend[i] - rstart[i]) for i,_ in enumerate(grid)}
    cstart = {}
    cend = {}
    csize = {}
    for c in range(mr):
        cstart[c] = list(grid[:, c]).index('.')
        cend[c] = mc - list(reversed(grid[:, c])).index('.')
        csize[c] = cend[c] - cstart[c]
    print(csize)
    r0, c0 = (0, rstart[0])
    grid[r0, c0] = 'x'

    dir = 'R'
    current = r0,c0

    for i, p in enumerate(path):
        if isinstance(p, int):
            print(f"Move in {dir}, {int(p)} steps")
            steps = int(p)
            match dir:
                case 'R':
                    row, col = current
                    s, grid[row, :] = walk(steps, grid[row, :])
                    current = (row, col + s)
                    print(current)
                case 'L':
                    row, col = current
                    s, grid[row, :] = walk(steps, reversed(grid[:[row]]))
                    current = (row, col - s)
                    print(current)

                case 'D':
                    row, col = current
                    s, grid[:, col] = walk(steps, grid[:, col])
                    current = (row + s, col)
                    print(current)

                case 'U':
                    row, col = current
                    s, grid[:, row] = walk(steps, reversed(grid[:, row]))
                    current = (row - s, col)
                    print(current)
        else:
            bdir = dir
            dir = rotate(dir, p)
            print(f"Rotate {p}: {bdir} -> {dir}")
        
        if i == 4:
            break 
    print(grid)

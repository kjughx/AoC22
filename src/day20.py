#!/bin/env python3

from itertools import cycle
import numpy as np

with open('inputs/test') as file:

    lines = [int(line.strip()) for line in file.readlines()]
    clines = lines.copy()


    """
    This maps an original index to a new index
    """
    mapon = np.array([i for i,_ in enumerate(lines)])
    
    mapno = np.array([mapon[i] for i,_ in enumerate(lines)])

    # # start with 0
    for i, line in enumerate(lines):
        mapon[i+1:i+line+1] = (mapon[i+1:i+line+1] - 1) % len(lines)
        mapon[i] = (mapon[i] + line) % len(lines)
        mapno[i+1:i+line+1] = (mapno[i+1:i+line+1] - 1) % len(lines)
        mapno[i] = (mapno[i] + line) % len(lines)
        print(mapno, mapon)


        clines[mapno[mapon[i]]]
        if i == 1:
            break


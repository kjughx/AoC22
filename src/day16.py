#!/bin/env python3 

def distance(bnode, enode, vertices):
    spt = {}

with open('inputs/test') as file:
    tunnels = {}
    valves = {'AA': 0}
    for line in file.readlines():
        line = line.strip('\n')
        valve = line.split(' ')[1]
        rate = int(line.split(' ')[4].split('=')[1].strip(';'))
        targets = [target.split(' ')[-1] for target in line.split('to')[1].split(',')]
        if rate > 0:
            valves[valve] = rate
        tunnels[valve] = targets

    root = 'AA'
    """
    start at 'AA' and visit it's neighbors.
    """

    bits = {key: i for i,key in enumerate(sorted(valves))}

    # # If you come in to this function with the same opened set and same valve as a previous iteration, we already know the best path and what point it gives
    vis = {}
    def f(valve, time, opened):
        if time == 0:
            return 0
       
        try:
            return vis[key]
        except:
            pass

        ans = 0
        if not (bit & opened):
            opened |= bit
            ans = max(ans, valves[valve]*(time-1) + f(valve, time - 1, opened)) # open the valve

        for neighbor in tunnels[valve]:
            ans = max(ans, f(neighbor, time-1, opened)) # go to neighbor

        vis[key] = ans 

        return ans


    print(f('AA', 30, 0))

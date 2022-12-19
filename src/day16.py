#!/bin/env python3 

def distance(bnode, enode, vertices):
    spt = {}

with open('../inputs/test') as file:
    tunnels = {}
    for line in file.readlines():
        line = line.strip('\n')
        name = line.split(' ')[1]
        rate = int(line.split(' ')[4].split('=')[1].strip(';'))
        if 'valves' in line:
            valves = line.split(' valves ')[1].split(' ')
        else:
            valves = line.split(' valve ')[1].split(' ')
        tunnels[name] = (rate, 'c', valves)

    nonzero = [tunnels for tunnel in tunnels if tunnels[tunnel][0] != 0]
    for tunnel in tunnels:
        print(tunnels[tunnel])




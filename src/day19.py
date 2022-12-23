#!/bin/env python3

with open('../inputs/day19') as file:
    for line in file.readlines():
        line = line.strip('\n')

def canBuy(material, rbts):
    for num, mat in rbts[material][0]:
        if rbts[mat][2] < int(num):
            return False
    return True

from collections import deque
import re

with open('inputs/day19') as file:
    blueprints = [line.strip('\n') for line in file.readlines()]
    quality = 0
    # for each minute, try buying or waiting and flood fill the queue 
    materials = ['ore', 'clay', 'obsidian', 'geode']
    for blueprint in blueprints:
        costs = [re.findall('\d \w+', line) for line in blueprint.split('.')]
        orer = [cost.split(' ') for cost in costs[0]]
        clayr = [cost.split(' ') for cost in costs[1]]
        obsr = [cost.split(' ') for cost in costs[2]]
        geor = [cost.split(' ') for cost in costs[3]]
        robots = {"ore": [orer, 0,0], "clay": [clayr, 0,0], "obsidian": [obsr, 0,0], "geode": [geor, 0,0]}

        q = deque([[robots, "ore", 'w']])
        while q:
            rbts, material, action = q.popleft()
            match action:
                case 'w':
                    rbts[material][2] += 1
                case 'b':
                    rbts[material][1] += 1
                    for num, mat in rbts[material][0]:
                        rbts[mat][2] -= int(num)
            for material in materials:
                if canBuy(material, rbts):
                    q.append([rbts.copy(), material, 'b'])
                else:
                    q.append([rbts.copy(), material, 'w'])
            print(q)
            break
>>>>>>> 3888ccc (No need to upload the inputs)

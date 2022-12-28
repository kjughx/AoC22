#!/bin/env python3

def wait(bots, resources):
    for i in range(len(bots)):
        resources[i] += bots[i]
    return bots, resources


def canBuy(material, costs, resources):
    for i, cost in enumerate(costs[material]):
        if resources[i] < cost:
            return False
    return True

def buy(material, costs, bots, resources):
    for i, cost in enumerate(costs[material]):
        resources[i] -= cost
    bots[material] += 1
    return bots, resources

import re

with open('inputs/day19') as file:
    blueprints = [line.strip('\n') for line in file.readlines()]
    quality = 0

    materials = ['ore', 'clay', 'obsidian', 'geode']
    for blueprint in blueprints:
        costs = [re.findall("\d+ \w+", line) for line in blueprint.split('. ')]
        bp = []
        for cost in costs:
            c = [int(m.split(' ')[0]) for m in cost]
            bp.append(c)

        costs = bp
        print(costs)

        vis = {}
        def f(time, bots, resources):
            if time == 0:
                return 0

            key = (time, *bots, *resources)
            if key in vis:
                return vis[key]

            ans = 0

            bots_, resources_ = wait(bots, resources)
            print(time, 'w', bots_, resources_)
            ans = max(ans, f(time-1, bots_, resources_))

            for i in range(len(materials)):
                if canBuy(i, costs, resources):
                    bots_, resources_ = buy(i, costs, bots, resources)
                    print(time, 'b', bots_, resources_)
                    ans = max(ans, f(time-1, bots_, resources_))

            ans = resources[3]
            vis[key] = ans
            return ans

        # print(f(10, [1, 0, 0, 0], [0,0,0,0]))

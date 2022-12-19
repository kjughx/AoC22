#!/bin/env python3 

from itertools import cycle
from collections import deque
import numpy as np

answers = [int(line.strip('\n')) for line in open('/home/philip/AoC22/src/answer').readlines()]
for i in range(2022):
    width = 7
    sidel = deque([])
    sider = deque([])
    mrow = [-1 for _ in range(width)]
    shapes = cycle(['-', '+', 'L', '|', '*'])
    line = cycle('>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>')
    first = True
    for _ in range(i+1):
        shape = next(shapes)
        h = 3 if first else max(mrow) + 4
        first = False

        if shape == '-':
            bot = deque([None, None, h, h, h, h, None])
            top = deque([None, None, h, h, h, h, None])
            xls = {h: 2}
            xrs = {h: 5}
        elif shape == '+':
            bot = deque([None, None, h+1, h, h+1, None, None])
            top = deque([None, None, h+1, h+2, h+1, None, None])
            xls = {h: 3, h+1: 2, h+2: 3}
            xrs = {h: 3, h+1: 4, h+2: 3}
        elif shape == 'L':
            bot = deque([None, None, h, h, h, None, None])
            top = deque([None, None, h, h, h+2, None, None])
            xls = {h: 2, h+1: 4, h+2: 4}
            xrs = {h: 4, h+1: 4, h+2: 4}
        elif shape == '|':
            bot = deque([None, None, h, None, None, None, None])
            top = deque([None, None, h+3, None, None, None, None])
            xls = {h: 2, h+1: 2, h+2: 2, h+3: 2}
            xrs = {h: 2, h+1: 2, h+2: 2, h+3: 2}
        elif shape == '*':
            bot = deque([None, None, h, h, None, None, None])
            top = deque([None, None, h+1, h+1, None, None, None])
            xls = {h: 2, h+1: 2}
            xrs = {h: 3, h+1: 3}

        falling = True
        print(bot)
        while falling:
            shift = next(line)
            if shift == '<' and bot[0] is None:
                for key, val in xls.items():
                    if key >= len(sidel):
                        continue
                    elif sidel[key] == val - 1:
                        break
                else:
                    bbot = bot.copy()
                    bbot.rotate(-1)
                    if not any(mh == bb for mh,bb in zip(mrow, bbot)):
                        bot.rotate(-1)
                        top.rotate(-1)
                        xls = {key: val - 1 for key,val in xls.items()}
                        xrs = {key: val - 1 for key,val in xrs.items()}

            elif shift == '>' and bot[-1] is None:
                for key, val in xrs.items():
                    if key >= len(sider):
                        continue
                    elif sider[key] == val + 1:
                        break
                else:
                    bbot = bot.copy()
                    bbot.rotate(1)
                    if not any(mh == bb for mh,bb in zip(mrow, bbot)):
                        bot.rotate(1)
                        top.rotate(1)
                        xls = {key: val + 1 for key,val in xls.items()}
                        xrs = {key: val + 1 for key,val in xrs.items()}

            if any(mh == ch - 1 or ch -1 == -1 if ch is not None else False for mh,ch in zip(mrow,bot)):
                # hit a stop
                mrow = [max(y1,y2 if y2 is not None else -1) for y1,y2 in zip(mrow, top)]
                print(shift, bot)
                print(mrow)
                for key, val in xls.items():
                    if key >= len(sidel):
                        sidel.append(val)
                    else:
                        sidel[key] = min(sidel[key], val)
                for key, val in xrs.items():
                    if key >= len(sider):
                        sider.append(val)
                    else:
                        sider[key] = max(sider[key], val)
                falling = False
                break
            else:
                bot = deque([y - 1 if y is not None else None for y in bot])
                top = deque([y - 1 if y is not None else None for y in top])
                xls = {max(0, key - 1): val if key-1 >= 0 else None for key,val in xls.items()}
                xrs = {max(0, key - 1): val if key-1 >= 0 else None for key,val in xrs.items()}
            print(shift, bot)
    answer = max(mrow)
    answer = 1 if answer == -1 else answer + 1
    print(mrow)

    if answer != answers[i]:
        print(i, answer, " != ", answers[i])
        break

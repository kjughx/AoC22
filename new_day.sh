#!/bin/sh

day=$(ls -d src/day* | sort | tail -n1 | sed 's/src\/day\(\w\+\)/\1/')
day=$((day + 1))
if [ ! -d "src/day$day" ]; then
    mkdir -p src/day$day
    cp template.py src/day$day/main.py
    sed -i "s/dayx/day$day/" src/day$day/main.py
    touch inputs/day$day
fi


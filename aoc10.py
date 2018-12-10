#!/usr/bin/env python3
import sys
import re
import time


def evaluate_area(points, t):
    '''Evaluate the area of the bounding points of points at time t.
    '''
    min_x = float('inf')
    min_y = float('inf')
    max_x = float('-inf')
    max_y = float('-inf')

    for point in points:
        pos = (point[0] + t * point[2], point[1] + t * point[3])
        min_x = min(min_x, pos[0])
        min_y = min(min_y, pos[1])
        max_x = max(max_x, pos[0])
        max_y = max(max_y, pos[1])

    return (max_x - min_x) * (max_y - min_y)


def area_decreasing(points, t):
    '''Check if the area of the bounds is decreasing between t and t+1. Performs
    two evaluations.
    '''
    return evaluate_area(points, t + 1) < evaluate_area(points, t)


def draw(points, t):
    '''Print the points at time t.
    '''
    min_x = float('inf')
    min_y = float('inf')
    max_x = float('-inf')
    max_y = float('-inf')

    positions = set()
    for point in points:
        pos = (point[0] + t * point[2], point[1] + t * point[3])
        min_x = min(min_x, pos[0])
        min_y = min(min_y, pos[1])
        max_x = max(max_x, pos[0])
        max_y = max(max_y, pos[1])
        positions.add(pos)

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            char = '#' if (x, y) in positions else '.'
            print(char, end='')
        print("")


def main():
    fname = sys.argv[1]

    # position=< 52763, -10408> velocity=<-5,  1>
    expr = re.compile(r'position=< *(-?\d+), *(-?\d+)> velocity=< *(-?\d+), *(-?\d+)>\n')

    # tuple (x, y, dx, dy)
    points = []

    with open(fname) as f:
        for line in f:
            m = re.fullmatch(expr, line)
            point = tuple(map(int, m.group(1, 2, 3, 4)))
            points.append(point)

    # Find lower bound
    t = 1
    while area_decreasing(points, t):
        print("Lower bound: t={}".format(t))
        lower = t
        t *= 2
    upper = t

    # Bisect
    while True:
        mid = lower + (upper - lower) // 2
        if area_decreasing(points, mid):
            lower = mid
        else:
            upper = mid

        print("Bounds: t={}...{} ".format(lower, upper))

        if upper - lower <= 1:
            break

    print("Sky at t={}:\n".format(upper))
    draw(points, upper)


if __name__ == '__main__':
    main()

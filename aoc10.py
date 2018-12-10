#!/usr/bin/env python3
import sys
import re
import time


def step(points):
    '''Updates points in place. Returns the bounding box of the sky (min, max).
    '''

    min_x = float('inf')
    min_y = float('inf')
    max_x = float('-inf')
    max_y = float('-inf')

    for i in range(len(points)):
        next_point = (
            points[i][0] + points[i][2],
            points[i][1] + points[i][3],
            points[i][2],
            points[i][3]
        )

        min_x = min(min_x, next_point[0])
        min_y = min(min_y, next_point[1])
        max_x = max(max_x, next_point[0])
        max_y = max(max_y, next_point[1])

        points[i] = next_point

    return ((min_x, min_y), (max_x, max_y))


def show(points, bounds):
    '''Print the sky area defined by bounds.
    '''

    positions = set(point[0:2] for point in points)

    for y in range(bounds[0][1], bounds[1][1] + 1):
        for x in range(bounds[0][0], bounds[1][0] + 1):
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

    # Step through time while the area if the bounding box of the points is
    # shrinking. Print out if area is smaller than 100*10.
    prev_area = float('inf')
    t = 1
    while True:
        bounds = step(points)
        height = bounds[1][1] - bounds[0][1]
        width = bounds[1][0] - bounds[0][0]
        area = width * height

        print("t={}, w={}, h={}".format(t, width, height))

        if area < 100 * 10:
            show(points, bounds)

        if area > prev_area:
            break

        t += 1
        prev_area = area


if __name__ == '__main__':
    main()

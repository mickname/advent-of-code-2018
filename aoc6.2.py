#!/usr/bin/env python3
import sys
import itertools


def find_bounds(coords):
    '''Find the bounding min and max points for the coordinate tuples.
    '''
    minx = coords[0][0]
    miny = coords[0][1]
    maxx = minx
    maxy = miny
    for x, y in coords[1:]:
        minx = min(minx, x)
        miny = min(miny, y)
        maxx = max(maxx, x)
        maxy = max(maxy, y)
    return ((minx, miny), (maxx, maxy))


def main():
    fname = sys.argv[1]
    # The maximum sum of manhattan distance. 32 for sample, 10k for real.
    max_distance = int(sys.argv[2])

    with open(fname) as f:
        original_coords = [tuple(map(int, line.split(', '))) for line in f]

    top_left, bottom_right = find_bounds(original_coords)
    w = bottom_right[0] - top_left[0] + 1
    h = bottom_right[1] - top_left[0] + 1

    # Shift the coordinates to start from (0, 0)
    coords = [(pos[0] - top_left[0], pos[1] - top_left[1]) for pos in original_coords]

    within_region = 0
    for pos in itertools.product(range(h), range(w)):
        distances = [abs(coord[0] - pos[0]) + abs(coord[1] - pos[1]) for coord in coords]
        if sum(distances) < max_distance:
            within_region += 1

    print("Total tiles in region: {}".format(within_region))


if __name__ == '__main__':
    main()

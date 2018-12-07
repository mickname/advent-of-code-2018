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


def find_closest(coords, pos):
    '''Find the closest coordinate tuple to the position pos, returning its
    index or None in case of a draw.
    '''
    distances = [abs(coord[0] - pos[0]) + abs(coord[1] - pos[1]) for coord in coords]
    closest = None
    best = None
    for i, dist in enumerate(distances):
        if best is None:
            closest = i
            best = dist
        elif dist == best:
            closest = None
        elif dist < best:
            closest = i
            best = dist
    return closest


def main():
    fname = sys.argv[1]

    with open(fname) as f:
        original_coords = [tuple(map(int, line.split(', '))) for line in f]

    top_left, bottom_right = find_bounds(original_coords)
    w = bottom_right[0] - top_left[0] + 1
    h = bottom_right[1] - top_left[0] + 1

    # Shift the coordinates to start from (0, 0)
    coords = [(pos[0] - top_left[0], pos[1] - top_left[1]) for pos in original_coords]

    # List of areas for each coordinate index. -1 will signify infinite area.
    areas = [0] * len(coords)

    for y, x in itertools.product(range(h), range(w)):
        closest_idx = find_closest(coords, (x, y))
        if closest_idx is not None:
            # Infinite area?
            if x == 0 or y == 0 or x == w - 1 or y == h - 1:
                areas[closest_idx] = -1
            elif areas[closest_idx] != -1:
                areas[closest_idx] += 1

    print("Largest finite area: {} tiles".format(max(areas)))


if __name__ == '__main__':
    main()

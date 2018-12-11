#!/usr/bin/env python3
import sys
import itertools

# Grid size
W = 300
H = 300


def cell_power(x, y, serial):
    rack_id = x + 10
    power = rack_id * y
    power += serial
    power *= rack_id
    hundreds = power // 100 % 10
    return hundreds - 5


def main():
    serial = int(sys.argv[1])

    grid = [0] * W * H

    for y, x in itertools.product(range(0, H), range(0, W)):
            grid[H * y + x] = cell_power(x + 1, y + 1, serial)

    # Find 3x3 square with largest sum
    largest_total = float('-inf')
    largest_pos = None
    for y, x in itertools.product(range(0, H - 2), range(0, W - 2)):
        total = sum(grid[H * (y + dy) + x + dx]
                    for dy, dx in itertools.product(range(0, 3), range(0, 3)))
        if total > largest_total:
            largest_total = total
            largest_pos = (x + 1, y + 1)

    print("Largest total power in {},{} with power = {}".format(*largest_pos, largest_total))


if __name__ == '__main__':
    main()

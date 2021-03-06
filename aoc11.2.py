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

    # Construct a separate (for no reason) integral image of the grid:
    integral = [0] * (W + 1) * (H + 1)
    for y, x in itertools.product(range(1, H + 1), range(1, W + 1)):
        left = integral[H * y + x - 1]
        top = integral[H * (y - 1) + x]
        top_left = integral[H * (y - 1) + x - 1]
        integral[H * y + x] = grid[H * (y - 1) + x - 1] + left + top - top_left

    # Find sxs square with largest sum. See earlier commits for a more readable
    # version.
    largest_total = float('-inf')
    largest_pos = None
    for s in range(1, 300):
        for y in range(0, H - s - 1):
            Hy = H * y
            Hys = H * (y + s)
            Hy_s = Hy + s
            Hys_s = Hys + s
            for x in range(0, W - s - 1):
                total = (
                    integral[Hys_s + x] + integral[Hy + x]
                    - integral[Hy_s + x] - integral[Hys + x]
                )
                if total > largest_total:
                    largest_total = total
                    largest_pos = (x + 1, y + 1, s)

    print("Largest total power in {},{},{} with power = {}".format(*largest_pos, largest_total))


if __name__ == '__main__':
    main()

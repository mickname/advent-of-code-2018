#!/usr/bin/env python3
import sys


CART_TO_TRACK = {
    '<': '-',
    '>': '-',
    '^': '|',
    'v': '|',
}

CART_TO_DIR = {
    '<': (-1, 0),
    '>': (1, 0),
    '^': (0, 1),
    'v': (0, -1),
}


def print_state(grid, w, h, carts):
    grid_with_carts = grid[:]
    for y, x, symbol in carts:
        grid_with_carts[w * y + x] = symbol
    print('\n'.join([''.join(grid_with_carts[w * row:w * row + w])
          for row in range(h)]))


def main():
    fname = sys.argv[1]

    grid = []
    carts = []

    with open(fname) as f:
        for row, line in enumerate(f):
            for col, char in enumerate(line):
                if char == '\n':
                    continue
                try:
                    grid.append(CART_TO_TRACK[char])
                    carts.append((row, col, char))
                except KeyError:
                    grid.append(char)

    width = col
    height = row + 1

    print("Grid size: {}, {}".format(width, height))

    for t in range(2):
        print("tick = {}".format(t))
        # Print grid
        print_state(grid, width, height, carts)
        print('')
        # Update cart locations
        carts.sort()
        for i, cart in enumerate(carts):
            pos = cart[0:2]
            vec = CART_TO_DIR(cart[2])
            new_pos = (pos[0] + vec[0], pos[1] + vec[1])


if __name__ == '__main__':
    main()

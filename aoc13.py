#!/usr/bin/env python3
import sys
import collections
from operator import itemgetter


Cart = collections.namedtuple('Cart', ['x', 'y', 'symbol', 'dx', 'dy', 'turn'])

CART_TO_TRACK = {
    '<': '-',
    '>': '-',
    '^': '|',
    'v': '|',
}

CART_TO_DIR = {
    '^': (0, -1),
    '>': (1, 0),
    'v': (0, 1),
    '<': (-1, 0),
}
DIR_TO_CART = {dir: symbol for symbol, dir in CART_TO_DIR.items()}


def print_state(grid, w, h, carts):
    grid_with_carts = grid[:]
    for c in carts:
        grid_with_carts[w * c.y + c.x] = c.symbol
    print('\n'.join([''.join(grid_with_carts[w * row:w * row + w])
          for row in range(h)]))


def new_dir(cart, track):
    if track == '+':
        dirs = ['^', '>', 'v', '<']
        new_symbol = dirs[(dirs.index(cart.symbol) + cart.turn) % 4]
        return (new_symbol, *CART_TO_DIR[new_symbol])
    elif track == '\\':
        dx = cart.dy
        dy = cart.dx
    elif track == '/':
        dx = -cart.dy
        dy = -cart.dx

    return (DIR_TO_CART[dx, dy], dx, dy)


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
                    carts.append(Cart(col, row, char, *CART_TO_DIR[char], -1))
                except KeyError:
                    grid.append(char)

    width = col
    height = row + 1

    print("Grid size: {}, {}".format(width, height))

    t = 0
    collision = False
    while not collision:
        print("tick = {}".format(t))
        # Print grid
        print_state(grid, width, height, carts)
        print('')
        t += 1
        # Update cart locations
        carts.sort(key=itemgetter(1, 0))
        for i, cart in enumerate(carts):
            x = cart.x + cart.dx
            y = cart.y + cart.dy
            # Check for collisions:
            for cart2 in carts:
                if x == cart2.x and y == cart2.y:
                    collision = True
                    break
            if collision:
                break

            symbol = cart.symbol
            dx = cart.dx
            dy = cart.dy
            turn = cart.turn

            at_pos = grid[width * y + x]
            if at_pos in ('/', '\\'):
                symbol, dx, dy = new_dir(cart, at_pos)
            if at_pos == '+':
                symbol, dx, dy = new_dir(cart, at_pos)
                turn = cart.turn + 1 if cart.turn < 1 else -1

            carts[i] = Cart(x, y, symbol, dx, dy, turn)

    print("Collision at x,y = {},{}".format(x, y))


if __name__ == '__main__':
    main()

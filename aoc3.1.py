#!/usr/bin/env python3
import sys
import collections

def main():
    fname = sys.argv[1]

    # How many times position (x, y) has been claimed? An array would be faster
    # for this small a problem..
    claims = collections.defaultdict(lambda: 0)

    with open(fname) as f:
        for line in f:
            # Example line:
            # #25 @ 872,224: 28x24
            _, _, position_str, dimension_str = line.split(' ')
            start_x, start_y = map(int, position_str[:-1].split(','))
            w, h = map(int, dimension_str[:-1].split('x'))

            for y in range(start_y, start_y + h):
                for x in range(start_x, start_x + w):
                    claims[(x, y)] += 1

    num_claimed_twice_or_more = 0
    for _, num_claims in claims.items():
        if num_claims >= 2:
            num_claimed_twice_or_more += 1

    print("Square inches with more than 1 claims: {}".format(num_claimed_twice_or_more))

if __name__ == '__main__':
    main()

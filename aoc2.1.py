#!/usr/bin/env python3
import sys
import collections

def main():
    fname = sys.argv[1]

    twos = 0
    threes = 0

    with open(fname) as f:
        for line in (line.rstrip() for line in f if line != '\n'):
            letter_count = collections.Counter(line)
            two_same = False
            three_same = False

            for _, count in letter_count.items():
                if count == 2:
                    two_same = True
                elif count == 3:
                    three_same = True

            if two_same:
                twos += 1
            if three_same:
                threes += 1

    print("Twice: {}, thrice: {}".format(twos, threes))
    print("Answer: {} * {} = {}".format(twos, threes, twos * threes))

if __name__ == '__main__':
    main()

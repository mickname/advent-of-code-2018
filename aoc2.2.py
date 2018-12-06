#!/usr/bin/env python3
import sys

def main():
    fname = sys.argv[1]

    encountered = set()
    with open(fname) as f:
        for line in (line.rstrip() for line in f if line != '\n'):
            # Insert the box id to the set of encountered ids, accounting for
            # all character removals
            for i in range(1, len(line)):
                ith_removed = line[:i-1] + line[i:]
                if (i, ith_removed) in encountered:
                    print("Found match: {}".format(ith_removed))

                encountered.add((i, ith_removed))

if __name__ == '__main__':
    main()

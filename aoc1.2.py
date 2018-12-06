#!/usr/bin/env python3
import sys
import itertools

def main():
    fname = sys.argv[1]
    with open(fname) as f:
        numbers = (int(line.rstrip()) for line in f if line != '\n')

        freq = 0
        encountered = set()
        for num in itertools.cycle(numbers):
            freq += num
            if freq in encountered:
                print(freq)
                break
            encountered.add(freq)

if __name__ == '__main__':
    main()

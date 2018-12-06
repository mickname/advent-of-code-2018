#!/usr/bin/env python3
import sys

def main():
    fname = sys.argv[1]
    with open(fname) as f:
        print(sum(int(line.rstrip()) for line in f if line != '\n'))

if __name__ == '__main__':
    main()

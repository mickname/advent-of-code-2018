#!/usr/bin/env python3
import sys
import itertools


def are_opposing_case(a, b):
    if a.lower() != b.lower():
        return False
    return a.isupper() != b.isupper()


def react(polymer):
    reacted = polymer[:]
    i = 0
    try:
        while True:
            if are_opposing_case(reacted[i], reacted[i+1]):
                reacted[i:] = reacted[i+2:]  # not gud
                i = max(0, i - 1)
            else:
                i += 1
    except IndexError:
        pass

    return reacted


def main():
    fname = sys.argv[1]
    with open(fname) as f:
        polymer = list(f.read().rstrip())
        reacted = react(polymer)

        # print(''.join(reacted))
        print("Polymer units remaining: {}".format(len(reacted)))


if __name__ == '__main__':
    main()

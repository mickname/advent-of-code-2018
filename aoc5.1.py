#!/usr/bin/env python3
import sys
import collections


def are_opposing_case(a, b):
    if a.lower() != b.lower():
        return False
    return a.isupper() != b.isupper()


def react(polymer):
    front = [polymer[0]]
    # Store the later values backwards to allow fast access to their original
    # front, now at the end of the list
    back = list(reversed(polymer[1:]))

    while back:
        if are_opposing_case(front[-1], back[-1]):
            front.pop()
            back.pop()
            if len(front) > 1:
                back.append(front.pop())
            elif len(front) == 0:
                front.append(back.pop())
        else:
            front.append(back.pop())

    return front


def main():
    fname = sys.argv[1]

    with open(fname) as f:
        polymer = list(f.read().rstrip())
        reacted = react(polymer)

        # print(''.join(reacted))
        print("Polymer units remaining: {}".format(len(reacted)))


if __name__ == '__main__':
    main()

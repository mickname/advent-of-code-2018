#!/usr/bin/env python3
import sys


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

    # Keep track of which unit types we have tried to remove
    removed_units = set()

    shortest_type = None
    shortest = None

    with open(fname) as f:
        polymer = list(f.read().rstrip())

        for unit in polymer:
            unit_type = unit.lower()
            if unit_type not in removed_units:
                removed_units.add(unit_type)
                # Find the length of the reacted polymer with unit_type removed:
                reacted = react([unit for unit in polymer if unit.lower() != unit_type])

                if shortest_type is None or len(reacted) < shortest:
                    shortest_type = unit_type
                    shortest = len(reacted)

    print("Shorted resulting polymer is {} units long, with unit type {}/{} removed."
          .format(shortest, shortest_type.upper(), shortest_type))


if __name__ == '__main__':
    main()

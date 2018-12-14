#!/usr/bin/env python3
import sys
import collections


def plants_to_str(state, rng):
    return ''.join([state[i] for i in rng])


def main():
    fname = sys.argv[1]

    # Hold the plant generation rules such as '.#... => #'.
    # The puzzle input has rules for all combinations of inputs, but the example
    # only has the ones that results in an alive plant, so use a defaultdict to
    # handle those as well.
    rules = collections.defaultdict(lambda: '.')

    # Store the state as a dict also :)
    state = collections.defaultdict(lambda: '.')

    # Keep track of the indices of bounds of the alive plant pots.
    first_alive = None
    last_alive = 0

    with open(fname) as f:
        # 'initial state: #.#.....\n'
        state_str = f.readline()[15:-1]
        for number, pot_state in enumerate(state_str):
            state[number] = pot_state
            if pot_state == '#':
                last_alive = number
                if first_alive is None:
                    first_alive = number

        # Read the rules
        for line in f:
            if line != '\n':
                input, _, output = line.split()
                rules[input] = output

    # Calculate next generation
    for g in range(20):
        new_state = collections.defaultdict(lambda: '.')
        for i in range(first_alive - 2, last_alive + 3):
            input = ''.join([state[x] for x in range(i - 2, i + 3)])
            output = rules[input]
            if output == '#':
                if i < first_alive:
                    first_alive = i
                if i > last_alive:
                    last_alive = i
            new_state[i] = output
        state = new_state

        print("{:2}: {}".format(g, plants_to_str(state, range(-3, last_alive + 1))))

    sum_of_ordinals = sum(i for i, p in state.items() if p == '#')
    print("Answer: {}".format(sum_of_ordinals))


if __name__ == '__main__':
    main()

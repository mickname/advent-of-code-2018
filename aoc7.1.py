#!/usr/bin/env python3
import sys


def main():
    fname = sys.argv[1]

    # Two dicts maintaing mapping from step 'A' to list of steps ['B', 'C', ...]
    steps_before = {}
    steps_after = {}

    # Parse input file
    with open(fname) as f:
        for line in f:
            # "Step C must be finished before step A can begin."
            tokens = line.split()
            before = tokens[1]
            after = tokens[7]

            try:
                steps_before[after].append(before)
            except KeyError:
                steps_before[after] = [before]

            try:
                steps_after[before].append(after)
            except KeyError:
                steps_after[before] = [after]

            if before not in steps_before:
                steps_before[before] = []

    execution = []
    try:
        while True:
            for step in sorted(steps_before.keys()):
                # No dependencies for this step? execute!
                if not steps_before[step]:
                    execution.append(step)
                    del steps_before[step]
                    # Raises KeyError if no more steps to do.
                    for after in steps_after[step]:
                        steps_before[after].remove(step)
                    del steps_after[step]
                    break
    except KeyError:
        pass

    print("Completion order:")
    print(''.join(execution))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import sys


def choose_step(steps_before, steps_after):
    '''Return the next step to begin work on, or None if all completed steps
    left. Modifies the input dictionaries.
    '''
    choice = None
    for step in sorted(steps_before.keys()):
        # No dependencies for this step? execute!
        if not steps_before[step]:
            choice = step
            del steps_before[step]
            break
    return choice


def complete_step(step, steps_before, steps_after):
    '''Mark step as completed and return True if there are steps remaining.
    '''
    try:
        for after in steps_after[step]:
            steps_before[after].remove(step)
        del steps_after[step]
        return True
    except KeyError:
        return False


def make_step_time_fn(base_time):
    def get_step_time(step):
        '''Return the number of seconds needeed to complete /step/.
        '''
        return ord(step) - ord('A') + 1 + base_time
    return get_step_time


def main():
    # usage: ./aoc7.2.py input7.txt 60 5
    fname = sys.argv[1]
    step_base_time = int(sys.argv[2])
    num_workers = int(sys.argv[3])

    get_step_time = make_step_time_fn(step_base_time)

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

    t = 0
    worker_step = [None] * num_workers
    worker_step_complete_at = [None] * num_workers

    while True:
        print("t={}".format(t))
        # Mark tasks complete
        for i in range(num_workers):
            if worker_step_complete_at[i] == t:
                print("Worker {} finished step {}".format(i, worker_step[i]))
                complete_step(worker_step[i], steps_before, steps_after)
                worker_step[i] = None
                worker_step_complete_at[i] = None
        # Assign new tasks
        for i in range(num_workers):
            if worker_step[i] is None:
                step = choose_step(steps_before, steps_after)
                if step is not None:
                    print("Worker {} starts step {}".format(i, step))
                    worker_step[i] = step
                    worker_step_complete_at[i] = t + get_step_time(step)
        # Jump to next time when a worker becomes available
        try:
            t = min(completion_time for completion_time in worker_step_complete_at
                    if completion_time is not None)
        except ValueError:
            break

    print("All steps completedin {} seconds.".format(t))


if __name__ == '__main__':
    main()

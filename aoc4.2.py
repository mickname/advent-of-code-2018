#!/usr/bin/env python3
import sys
import collections
import operator

def main():
    fname = sys.argv[1]
    guard_id = None
    sleep_start_minute = None

    # Track how many times each minute was slept on by a specific guard.
    times_slept = collections.defaultdict(lambda: [0]*60)

    # guard most frequenltly asleep on the same minute, and how many minutes
    most_consistent_guard = None
    chosen_minute = None
    minutes_slept = 0

    with open(fname) as f:
        for line in sorted(temp for temp in f):
            # Parse the line:
            # [1518-11-01 23:58] Guard #99 begins shift
            #            /     | |    \ \ \
            #          time frag keyword param
            time_fragment, keyword, param = line.split(" ")[1:4]
            minute = int(time_fragment[3:5])

            if keyword == 'Guard':
                guard_id = int(param[1:])

            if keyword == 'falls':
                sleep_start_minute = minute
            elif keyword == 'wakes':
                # Increment each individual minute slept.
                for slept_minute in range(sleep_start_minute, minute):
                    accumulated = times_slept[guard_id][slept_minute] + 1
                    times_slept[guard_id][slept_minute] = accumulated
                    if accumulated > minutes_slept:
                        most_consistent_guard = guard_id
                        chosen_minute = slept_minute
                        minutes_slept = accumulated

    print("Most frequently asleep on the same minute was guard #{} with {} times.".format(
        most_consistent_guard,
        minutes_slept
    ))
    print("Answer: {} * {} = {}".format(
        most_consistent_guard,
        chosen_minute,
        most_consistent_guard*chosen_minute
    ))


if __name__ == '__main__':
    main()

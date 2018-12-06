#!/usr/bin/env python3
import sys
import collections
import operator

def main():
    fname = sys.argv[1]
    guard_id = None
    sleep_start_minute = None

    # Track how many minutes in total a guard by id has slept.
    total_minutes_slept = collections.defaultdict(lambda: 0)
    # Track how many times each minute was slept on by a specific guard.
    times_slept = collections.defaultdict(lambda: [0]*60)

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
                duration = minute - sleep_start_minute
                # Increment the total minutes slept and each individual minute
                # slept.
                total_minutes_slept[guard_id] += duration
                for slept_minute in range(sleep_start_minute, minute):
                    times_slept[guard_id][slept_minute] += 1

    # Find the guard that slept the most
    sleeper, slept = max(total_minutes_slept.items(), key=operator.itemgetter(1))
    print("The biggest sleeper is guard #{} with {} minutes slept.".format(sleeper, slept))

    # Find the minute the sleeper was most often sleeping on.
    minute, times_slept = max(enumerate(times_slept[sleeper]), key=operator.itemgetter(1))
    print("He was most often sleeping on minute {}, total {} times.".format(minute, times_slept))

    print("Answer: {} * {} = {}".format(sleeper, minute, sleeper*minute))

if __name__ == '__main__':
    main()

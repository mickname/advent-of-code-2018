#!/usr/bin/env python3
import sys


class Marble:
    def __init__(self, value):
        self.value = value
        self.cw = None
        self.ccw = None

    def place(self, other):
        '''Inserts a new marble in the circle according to the stupid elven
        rules. Returns the new current marble.
        '''
        before = self.cw
        after = self.cw.cw

        # print("before {}, after {}".format(before.value, after.value))

        other.ccw = before
        other.cw = after

        before.cw = other
        after.ccw = other

        return other

    def remove(self):
        '''Remove the marble 7 marbles ccw from this. Returns tuple of
        (new current marble, value of removed)
        '''
        removed = self
        for _ in range(7):
            removed = removed.ccw

        before = removed.ccw
        after = removed.cw
        before.cw = after
        after.ccw = before

        return (after, removed.value)


def main():
    try:
        num_players = int(sys.argv[1])
        num_marbles = int(sys.argv[2])
    except (IndexError, ValueError):
        print("Usage: {} NUM_PLAYERS NUM_MARBLES".format(sys.argv[0]), file=sys.stderr)
        return

    scores = [0] * num_players

    m = Marble(0)
    m.cw = m
    m.ccw = m

    player = 0
    for value in range(1, num_marbles + 1):
        if value % 23 != 0:
            m = m.place(Marble(value))
        else:
            (m, removed) = m.remove()
            scores[player] += value + removed

        player = (player + 1) % num_players

    print("High score: {}".format(max(scores)))


if __name__ == '__main__':
    main()

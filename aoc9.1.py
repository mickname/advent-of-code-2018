#!/usr/bin/env python3
import sys


def main():
    try:
        num_players = int(sys.argv[1])
        num_marbles = int(sys.argv[2])
    except (IndexError, ValueError):
        print("Usage: {} NUM_PLAYERS NUM_MARBLES".format(sys.argv[0]), file=sys.stderr)
        return

    scores = [0] * num_players

    marbles = [0]
    current_marble = 0  # index of ...
    player = 0
    for marble in range(1, num_marbles + 1):
        if marble % 23 != 0:
            current_marble = (current_marble + 2) % len(marbles)
            # Make consistent with example:
            if current_marble == 0:
                current_marble = len(marbles)
            marbles.insert(current_marble, marble)
        else:
            # Remove the marble 7 ccw from current
            idx_to_remove = (current_marble - 7) % len(marbles)
            removed = marbles[idx_to_remove]
            del marbles[idx_to_remove]
            # Increase the player's score by the number of the marble that would
            # have been placed and the removed marble.
            scores[player] += marble + removed

            current_marble = idx_to_remove % len(marbles)

        player = (player + 1) % num_players

    print("High score: {}".format(max(scores)))


if __name__ == '__main__':
    main()

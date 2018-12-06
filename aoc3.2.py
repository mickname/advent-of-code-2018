#!/usr/bin/env python3
import sys
import collections

def main():
    fname = sys.argv[1]

    # Set of claim ids for each claimed position (x, y).
    claims = collections.defaultdict(set)
    # The set of claim ids that are not sharing area with any other claim
    solo_claims = set()

    with open(fname) as f:
        for line in f:
            # Example line:
            # #25 @ 872,224: 28x24
            claim_id_str, _, position_str, dimension_str = line.split(' ')
            claim_id = int(claim_id_str[1:])
            start_x, start_y = map(int, position_str[:-1].split(','))
            w, h = map(int, dimension_str[:-1].split('x'))

            no_collision = True
            for y in range(start_y, start_y + h):
                for x in range(start_x, start_x + w):
                    claims_here = claims[(x, y)]
                    if claims_here:
                        no_collision = False
                        # Remove from solo claims: (actually there can only be one..)
                        if len(claims_here) == 1:
                            try:
                                solo_claims.remove(next(iter(claims[(x, y)])))
                            except KeyError:
                                pass

                    claims_here.add(claim_id)

            if no_collision:
                solo_claims.add(claim_id)

    print("Claim IDs with no collisions: {}".format(solo_claims))

if __name__ == '__main__':
    main()

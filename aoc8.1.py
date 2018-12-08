#!/usr/bin/env python3
import sys
import collections
import itertools

Node = collections.namedtuple('Node', ['num_children', 'num_meta', 'children', 'meta', 'size'])


def parse_node(tokens, start=0):
    '''Recursively parse the tokens, returning a parsed Node named tuple.
    '''
    # Header
    num_children = tokens[start + 0]
    num_meta = tokens[start + 1]
    children = []
    # Loop over the children
    offset = 2
    for _ in range(num_children):
        c = parse_node(tokens, start=start + offset)
        offset += c.size
        children.append(c)

    return Node(
        num_children=num_children,
        num_meta=num_meta,
        children=children,
        meta=tokens[start + offset:start + offset + num_meta],
        size=offset + num_meta
    )


def sum_of_meta(node):
    total = sum(node.meta)
    for c in node.children:
        total += sum_of_meta(c)
    return total


def main():
    fname = sys.argv[1]

    with open(fname) as f:
        tokens = list(map(int, f.read().split(" ")))

    root = parse_node(tokens)
    print("Sum of metadata entries: {} ".format(sum_of_meta(root)))


if __name__ == '__main__':
    main()

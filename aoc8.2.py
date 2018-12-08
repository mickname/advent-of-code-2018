#!/usr/bin/env python3
import sys
import collections
import itertools

Node = collections.namedtuple('Node', ['children', 'meta', 'size'])


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
        children=children,
        meta=tokens[start + offset:start + offset + num_meta],
        size=offset + num_meta
    )


def value_of_node(node):
    if not node.children:
        return sum(node.meta)
    acc = 0
    for ref in node.meta:
        if ref != 0 and ref <= len(node.children):
            acc += value_of_node(node.children[ref - 1])
    return acc


def main():
    fname = sys.argv[1]

    with open(fname) as f:
        tokens = list(map(int, f.read().split(" ")))

    root = parse_node(tokens)
    print("Value of root node: {} ".format(value_of_node(root)))


if __name__ == '__main__':
    main()

#!/usr/bin/env python

import sys

def process_node(node, value, adjacency_list=''):
    print(f'{node}\tNODE\t{value}\t{adjacency_list}')

    if adjacency_list:
        neighbors = adjacency_list.split(',')
        rank = value / len(neighbors)

        for neighbor in neighbors:
            print(f'{neighbor}\tVALUE\t{rank}\t{node}')

def mapper():
    for line in sys.stdin:
        parts = line.strip().split()

        node = parts[0]
        value = float(parts[1])
        adjacency_list = parts[2] if len(parts) > 2 else ''

        process_node(node, value, adjacency_list)

if __name__ == "__main__":
    mapper()

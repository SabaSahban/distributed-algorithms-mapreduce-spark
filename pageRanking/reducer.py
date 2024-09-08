#!/usr/bin/env python

import sys

def calculate_page_rank(alpha, graph_size, sum_ranks):
    return alpha / graph_size + (1 - alpha) * sum_ranks

def process_node(current_page, current_adjacency_list, sum_ranks, alpha, graph_size):
    new_rank = calculate_page_rank(alpha, graph_size, sum_ranks)
    print(f'{current_page}\t{new_rank}\t{current_adjacency_list}')
    return None, '', 0.0

def reducer(graph_size):
    alpha = 0.8
    current_page = None
    current_adjacency_list = ''
    sum_ranks = 0.0

    for line in sys.stdin:
        page_id, node_type, *other_parts = line.strip().split('\t')

        if page_id != current_page:
            if current_page is not None:
                current_page, current_adjacency_list, sum_ranks = process_node(
                    current_page, current_adjacency_list, sum_ranks, alpha, graph_size
                )

            if node_type == 'NODE':
                current_page = page_id
                current_adjacency_list = other_parts[1] if len(other_parts) > 1 else ''
                sum_ranks = 0.0

        elif node_type == 'VALUE':
            sum_ranks += float(other_parts[0])

    if current_page is not None:
        process_node(current_page, current_adjacency_list, sum_ranks, alpha, graph_size)

if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        graph_size = sum(1 for line in file)
    reducer(graph_size)

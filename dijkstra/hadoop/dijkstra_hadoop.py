from typing import List, Dict


def mapper(input_graph: Dict) -> List:
    output = []

    for node in input_graph.items():
        nid = node[0]
        distance = node[1][0]
        neighbors = node[1][1]
        path = node[1][2]

        if len(path) > 0 and path[len(path) - 1] != nid:
            path.append(nid)
        elif len(path) == 0:
            path.append(nid)

        output.append([nid, distance, neighbors, path])
        path = node[1][2]
        if len(neighbors) > 0:
            for neighbor in neighbors:
                if neighbor[0] is nid:
                    continue
                neighbor_path = path[:] + [neighbor[0]]
                neighbor_distance = distance + neighbor[1]
                output.append([neighbor[0], neighbor_distance, None, neighbor_path])

    return output


def shuffle_and_sort(input_graph: List) -> Dict:
    output = {}

    for line in input_graph:
        body = [
            line[1],
            line[2],
            line[3]
        ]
        if line[0] not in output:
            output[line[0]] = [body]
        else:
            output[line[0]].append(body)

    return output


def reducer(input_graph: Dict) -> Dict:
    output = {}
    for node in input_graph.items():
        min_distance = float('inf')
        nid = node[0]
        neighbors = []
        path = []
        for possibility in node[1]:
            distance = possibility[0]
            if possibility[1] is not None:
                neighbors = possibility[1]
            if distance < min_distance:
                min_distance = distance
                path = possibility[2]
        output[nid] = [
            min_distance,
            neighbors,
            path
        ]
    return output


def prepare_data(input_graph: List) -> Dict:
    output = {}
    initial_node = True
    for line in input_graph:
        if line[0] not in output:
            output[line[0]] = [
                0 if initial_node else 9999,
                [],
                []
            ]
            output[line[0]][1].append([line[1], line[2]])
            initial_node = False
        else:
            output[line[0]][1].append([line[1], line[2]])

        if line[1] not in output:
            output[line[1]] = [
                9999,
                [],
                []
            ]

    return output


def dijkstra(input_graph: List) -> Dict:
    graph = prepare_data(input_graph)

    for i in range(6):
        graph = mapper(graph)
        graph = shuffle_and_sort(graph)
        graph = reducer(graph)

    return graph

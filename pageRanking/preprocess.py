from graph import graph

file_path = "input.txt"

def format_adjacency_list(adjacency_list):
    return ",".join(adjacency_list) if adjacency_list else ''

with open(file_path, "w") as file:
    for node, data in graph.items():
        page_rank = data.get("PageRank", 0.0)
        adjacency_list = format_adjacency_list(data.get("AdjacencyList", []))
        line = f"{node} {page_rank} {adjacency_list}\n"
        file.write(line)

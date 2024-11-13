import numpy as np


def build_incidence_matrix(graph):
 # A NumPy array representing the incidence matrix.

    vertices = list(graph.keys())
    edges = [(v1, v2) for v1 in vertices for v2 in graph[v1] if v1 < v2]
    matrix = np.zeros((len(vertices), len(edges)))
    for i, edge in enumerate(edges):
        v1, v2 = edge
        matrix[vertices.index(v1), i] = 1
        matrix[vertices.index(v2), i] = 1
    return matrix


# Example usage
graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "E"],
    "D": ["B"],
    "E": ["C"],
}
incidence_matrix = build_incidence_matrix(graph)
print(incidence_matrix)

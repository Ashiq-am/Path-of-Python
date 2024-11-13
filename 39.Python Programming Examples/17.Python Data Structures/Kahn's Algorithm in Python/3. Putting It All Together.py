# Example usage
def main():
    # Number of nodes in the graph
    n = 6
    # List of edges in the graph
    edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]

    # Create a graph with n nodes
    graph = Graph(n)

    # Add edges to the graph
    for u, v in edges:
        graph.add_edge(u, v)

    # Perform topological sort using Kahn's Algorithm
    topological_order = kahn_topological_sort(graph)

    print("Topological Order:", topological_order)


if __name__ == "__main__":
    main()

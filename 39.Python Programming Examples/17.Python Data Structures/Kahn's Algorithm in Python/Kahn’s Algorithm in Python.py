from collections import defaultdict, deque


class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
        self.in_degree = [0] * n

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.in_degree[v] += 1


def kahn_topological_sort(graph):
    # Queue to hold nodes with no incoming edges
    queue = deque([node for node in range(graph.n) if graph.in_degree[node] == 0])

    topological_order = []

    while queue:
        node = queue.popleft()
        topological_order.append(node)

        # For each outgoing edge from the current node
        for neighbor in graph.graph[node]:
            # Decrease the in-degree of the neighbor
            graph.in_degree[neighbor] -= 1
            # If the neighbor has no other incoming edges, add it to the queue
            if graph.in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check if topological sorting is possible (graph should have no cycles)
    if len(topological_order) == graph.n:
        return topological_order
    else:
        # If not all nodes are in topological order, there is a cycle
        return "Graph has at least one cycle"


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

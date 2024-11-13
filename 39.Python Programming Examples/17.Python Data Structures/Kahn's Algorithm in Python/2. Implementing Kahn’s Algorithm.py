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

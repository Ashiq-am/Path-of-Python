def boruvkas_algorithm(graph):
    V, edges = graph.V, graph.graph
    disjoint_set = DisjointSet(V)

    mst = []
    num_of_components = V

    while num_of_components > 1:
        cheapest = [-1] * V

        for u, v, w in edges:
            set_u = disjoint_set.find(u)
            set_v = disjoint_set.find(v)

            if set_u != set_v:
                if cheapest[set_u] == -1 or cheapest[set_u][2] > w:
                    cheapest[set_u] = [u, v, w]
                if cheapest[set_v] == -1 or cheapest[set_v][2] > w:
                    cheapest[set_v] = [u, v, w]

        for node in range(V):
            if cheapest[node] != -1:
                u, v, w = cheapest[node]
                set_u = disjoint_set.find(u)
                set_v = disjoint_set.find(v)

                if set_u != set_v:
                    mst.append([u, v, w])
                    disjoint_set.union(set_u, set_v)
                    num_of_components -= 1

    return mst

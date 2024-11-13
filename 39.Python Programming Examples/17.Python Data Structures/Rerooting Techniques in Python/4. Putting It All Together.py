def sum_of_distances_in_tree(n, edges):
    tree = Tree(n)
    for u, v in edges:
        tree.add_edge(u, v)

    dp = [0] * n
    subtree_size = [1] * n
    result = [0] * n

    # Initial DFS from node 0
    dfs(0, -1, tree, dp, subtree_size)

    # Rerooting to calculate the result for all nodes
    reroot(0, -1, tree, dp, subtree_size, result)

    return result


# Example usage
n = 6
edges = [(0, 1), (0, 2), (2, 3), (2, 4), (2, 5)]
print(sum_of_distances_in_tree(n, edges))

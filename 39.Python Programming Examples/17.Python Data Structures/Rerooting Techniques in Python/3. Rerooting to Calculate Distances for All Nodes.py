def reroot(node, parent, tree, dp, subtree_size, result):
    result[node] = dp[node]
    for neighbor in tree.graph[node]:
        if neighbor == parent:
            continue
        # Move root from node to neighbor
        dp[node] -= dp[neighbor] + subtree_size[neighbor]
        subtree_size[node] -= subtree_size[neighbor]
        dp[neighbor] += dp[node] + subtree_size[node]
        subtree_size[neighbor] += subtree_size[node]

        # Recursively reroot
        reroot(neighbor, node, tree, dp, subtree_size, result)

        # Restore original values
        subtree_size[neighbor] -= subtree_size[node]
        dp[neighbor] -= dp[node] + subtree_size[node]
        subtree_size[node] += subtree_size[neighbor]
        dp[node] += dp[neighbor] + subtree_size[neighbor]

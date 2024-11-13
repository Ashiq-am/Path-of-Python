def dfs(node, parent, tree, dp, subtree_size):
    for neighbor in tree.graph[node]:
        if neighbor == parent:
            continue
        dfs(neighbor, node, tree, dp, subtree_size)
        subtree_size[node] += subtree_size[neighbor]
        dp[node] += dp[neighbor] + subtree_size[neighbor]

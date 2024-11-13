from collections import defaultdict


class Tree:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)


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


def dfs(node, parent, tree, dp, subtree_size):
    for neighbor in tree.graph[node]:
        if neighbor == parent:
            continue
        dfs(neighbor, node, tree, dp, subtree_size)
        subtree_size[node] += subtree_size[neighbor]
        dp[node] += dp[neighbor] + subtree_size[neighbor]


# function to find the sum of distances from each node to all other nodes
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

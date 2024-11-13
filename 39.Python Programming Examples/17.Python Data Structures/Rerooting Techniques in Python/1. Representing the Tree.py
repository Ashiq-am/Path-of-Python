from collections import defaultdict


class Tree:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = []  # List to store graph edges

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def boruvka_mst(self):
        parent = []
        rank = []

        mst_weight = 0
        num_of_trees = self.V
        mst_edges = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while num_of_trees > 1:
            cheapest = [-1] * self.V

            for u, v, w in self.graph:
                set1 = self.find(parent, u)
                set2 = self.find(parent, v)

                if set1 != set2:
                    if cheapest[set1] == -1 or cheapest[set1][2] > w:
                        cheapest[set1] = [u, v, w]

                    if cheapest[set2] == -1 or cheapest[set2][2] > w:
                        cheapest[set2] = [u, v, w]

            for node in range(self.V):
                if cheapest[node] != -1:
                    u, v, w = cheapest[node]
                    set1 = self.find(parent, u)
                    set2 = self.find(parent, v)

                    if set1 != set2:
                        mst_weight += w
                        self.union(parent, rank, set1, set2)
                        mst_edges.append([u, v, w])
                        num_of_trees -= 1

        print("Weight of MST is", mst_weight)
        print("Edges in MST are:")
        for u, v, weight in mst_edges:
            print(f"{u} -- {v} == {weight}")

# Example usage
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

g.boruvka_mst()

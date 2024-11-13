class BipartiteGraph:
    def __init__(self):

        self.U = set()  # First set of vertices
        self.V = set()  # Second set of vertices
        self.adj_list = {}  # Adjacency list to store edges

    def add_vertex(self, vertex, set_type):

        if set_type == 'U':
            self.U.add(vertex)
        elif set_type == 'V':
            self.V.add(vertex)
        else:
            raise ValueError("set_type must be either 'U' or 'V'")
        # Initialize the adjacency list for the new vertex
        self.adj_list[vertex] = []

    def add_edge(self, u, v):

        if (u in self.U and v in self.V) or (u in self.V and v in self.U):
            self.adj_list[u].append(v)  # Add v to the adjacency list of u
            self.adj_list[v].append(u)  # Add u to the adjacency list of v
        else:
            raise ValueError("Edge must connect vertices from different sets")

    def is_bipartite(self):

        color = {}  # Dictionary to store the color of each vertex
        for vertex in list(self.U) + list(self.V):
            if vertex not in color:  # If the vertex has not been colored
                if not self._bfs_check(vertex, color):
                    return False  # If BFS finds the graph is not bipartite
        return True  # All vertices are colored successfully in two colors

    def _bfs_check(self, start, color):

        from collections import deque
        queue = deque([start])  # Initialize the queue with the starting vertex
        color[start] = 0  # Start coloring with color 0

        while queue:
            vertex = queue.popleft()
            current_color = color[vertex]

            for neighbor in self.adj_list[vertex]:
                if neighbor not in color:
                    color[neighbor] = 1 - current_color  # Alternate color
                    queue.append(neighbor)
                elif color[neighbor] == current_color:
                    return False  # If the neighbor has the same color, the graph is not bipartite

        return True  # All vertices are successfully colored

    def display(self):
        print("Set U:", self.U)
        print("Set V:", self.V)
        print("Adjacency List:")
        for vertex, neighbors in self.adj_list.items():
            print(f"{vertex}: {neighbors}")


# Example usage:
graph = BipartiteGraph()
graph.add_vertex('A', 'U')
graph.add_vertex('B', 'U')
graph.add_vertex('1', 'V')
graph.add_vertex('2', 'V')

graph.add_edge('A', '1')
graph.add_edge('A', '2')
graph.add_edge('B', '1')

graph.display()

if graph.is_bipartite():
    print("The graph is bipartite.")
else:
    print("The graph is not bipartite.")

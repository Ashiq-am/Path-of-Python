class BipartiteGraph:
    def __init__(self):
        """
        Initialize the bipartite graph with two sets of vertices and an adjacency list.
        """
        self.U = set()  # First set of vertices
        self.V = set()  # Second set of vertices
        self.adj_list = {}  # Adjacency list to store edges

# import networkx library
import networkx as nx

# create an empty undirected graph
G = nx.Graph()

# adding edge in graph G
G.add_edge(1, 2)
G.add_edge(2, 3, weight=0.9)

# import networkx library
import networkx as nx

# create an empty undirected graph
G = nx.Graph()

# add edge to the graph
G.add_edge('1', '2')
G.add_edge('2', '3')

# print the adjacent vertices
print(G.adj)

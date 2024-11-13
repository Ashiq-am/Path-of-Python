# importing networkx module
import networkx as nx

# creating sample graph object
G = nx.path_graph(7)

# creating sample graph object
H = nx.path_graph(3)

# compose of G and H saving in R
R = nx.compose(G,H)

# calling draw() to visualize the complement graph
nx.draw(R)

# import required module
import networkx

# number of nodes
n = 5

# create object
G = networkx.wheel_graph(n)

# illustrate graph
networkx.draw(G)

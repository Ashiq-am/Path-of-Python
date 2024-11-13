# import required module
import networkx as nx

# create object
G = nx.star_graph(10)

# illustrate graph
nx.draw(G, node_color = 'green',
		node_size = 100)

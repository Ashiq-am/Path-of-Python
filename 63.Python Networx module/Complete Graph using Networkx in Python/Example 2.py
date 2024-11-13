# import required module
import networkx

# create object
G = networkx.complete_graph(10)

# illustrate graph
networkx.draw(G, node_color = 'green',
			node_size = 1500)

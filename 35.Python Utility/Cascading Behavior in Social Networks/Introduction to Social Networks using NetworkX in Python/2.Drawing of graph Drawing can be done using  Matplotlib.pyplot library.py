# import matplotlib.pyplot library
import matplotlib.pyplot as plt

# import networkx library
import networkx as nx

# create a cubical empty graph
G = nx.cubical_graph()

# plotting the graph
plt.subplot(122)

# draw a graph with red
# node and vlue edge color
nx.draw(G, pos = nx.circular_layout(G),
		node_color = 'r',
		edge_color = 'b')

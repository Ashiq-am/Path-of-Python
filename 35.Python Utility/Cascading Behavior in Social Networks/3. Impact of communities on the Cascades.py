import networkx as nx
import random
import matplotlib.pyplot as plt


def first_community(G):
	for i in range(1, 11):
		G.add_node(i)
	for i in range(1, 11):
		for j in range(1, 11):
			if (i < j):
				r = random.random()
				if (r < 0.5):
					G.add_edge(i, j)
	return G

def second_community(G):
	for i in range(11, 21):
		G.add_node(i)
	for i in range(11, 21):
		for j in range(11, 21):
			if (i < j):
				r = random.random()
				if (r < 0.5):
					G.add_edge(i, j)
	return G


G = nx.Graph()
G = first_community(G)
G = second_community(G)
G.add_edge(5, 15)

nx.draw(G, with_labels=1)
plt.show()

nx.write_gml(G, "community.gml")

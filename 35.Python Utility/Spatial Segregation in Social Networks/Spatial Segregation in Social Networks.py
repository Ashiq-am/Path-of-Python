#import modules
import networkx as nx
import matplotlib.pyplot as plt
import random

# grid dimension
n = 10

# Building the graph
g = nx.grid_2d_graph(10, 10)
pos = dict((s, s) for s in g.nodes())
labels = dict(((i, j), i * 10 + j) for i, j in g.nodes())

# Display the graph in grid form.
def display(g):
	nodes_g = nx.draw_networkx_nodes(
		g, pos, node_color='green', nodelist=type1_node_list)
	nodes_r = nx.draw_networkx_nodes(
		g, pos, node_color='red', nodelist=type2_node_list)
	nodes_w = nx.draw_networkx_nodes(
		g, pos, node_color='white', nodelist=empty_cells)
	nx.draw_networkx_edges(g, pos)
	nx.draw_networkx_labels(g, pos, labels=labels)
	plt.show()


# Get the boundary nodes in the graph as boundary nodes have only 6 neighbors.
def get_boundary(g):
	boundary_nodes_list = []
	for ((u, v), d) in g.nodes(data=True):
		if (u == 0 or v == n - 1 or u == n - 1 or v == 0):
			boundary_nodes_list.append((u, v))
	return boundary_nodes_list


# Get internal neighbors.
def get_internal_neigh(u, v):
	return (
		[(u - 1, v), (u + 1, v), (u, v - 1), (u, v + 1), (u - 1, v + 1),
		(u + 1, v - 1), (u - 1, v - 1), (u + 1, v + 1)])


# Get boundary neighbors.
def get_boundary_neigh(u, v):
	if (u == 0 and v == 0):
		return ([(0, 1), (1, 1), (1, 0)])
	elif (u == n - 1 and v == n - 1):
		return ([(n - 2, n - 2), (n - 1, n - 2), (n - 2, n - 1)])
	elif (u == n - 1 and v == 0):
		return ([(u - 1, v), (u, v + 1), (u - 1, v + 1)])
	elif (u == 0 and v == n - 1):
		return ([(u + 1, v), (u + 1, v - 1), (u, v - 1)])
	elif (u == 0):
		return ([(u, v - 1), (u, v + 1), (u + 1, v), (u + 1, v - 1), (u + 1, v + 1)])
	elif (v == n - 1):
		return ([(u, v - 1), (u - 1, v), (u + 1, v), (u - 1, v - 1), (u + 1, v - 1)])
	elif (u == n - 1):
		return ([(u - 1, v), (u, v - 1), (u, v + 1), (u - 1, v + 1), (u - 1, v - 1)])
	elif (v == 0):
		return ([(u - 1, v), (u + 1, v), (u, v + 1), (u - 1, v + 1), (u + 1, v + 1)])


# Get the list of unsatisfied nodes in the graph.
def get_unsatisfied_nodes_list(g, internal_nodes_list, boundary_nodes_list):
	unsatisfied_nodes_list = []
	t = 3
	for u, v in g.nodes():
		type_of_this_node = g.nodes[(u, v)]['type']

		if (type_of_this_node == 0):
			continue
		else:
			similar_nodes = 0
			if ((u, v) in internal_nodes_list):
				neigh = get_internal_neigh(u, v)
			elif ((u, v) in boundary_nodes_list):
				neigh = get_boundary_neigh(u, v)

			for each in neigh:
				if (g.nodes[each]['type'] == type_of_this_node):
					similar_nodes += 1
			if (similar_nodes <= t):
				unsatisfied_nodes_list.append((u, v))

	return unsatisfied_nodes_list


# Make the node satisfied by shifting the position
# of unsatisfied node randomly and check if it becomes satisfied.
def make_a_node_satisfied(unsatisfied_nodes_list, empty_cells):
	if (len(unsatisfied_nodes_list) != 0):
		node_to_shift = random.choice(unsatisfied_nodes_list)
		new_position = random.choice(empty_cells)

		g.nodes[new_position]['type'] = g.nodes[node_to_shift]['type']
		g.nodes[node_to_shift]['type'] = 0
		labels[node_to_shift], labels[new_position] = labels[new_position],
		labels[node_to_shift]
	else:
		pass


# for adding diagonal edges
for (u, v) in g.nodes():
	if (u + 1 <= n - 1 and v + 1 <= n - 1):
		g.add_edge((u, v), (u + 1, v + 1))
	if (u + 1 <= n - 1 and v - 1 >= 0):
		g.add_edge((u, v), (u + 1, v - 1))


for ni in g.nodes():
	g.nodes[ni]['type'] = random.randint(0, 2)

type1_node_list = [ni for (ni, d) in g.nodes(data=True) if d['type'] == 1]
type2_node_list = [ni for (ni, d) in g.nodes(data=True) if d['type'] == 2]
empty_cells = [ni for (ni, d) in g.nodes(data=True) if d['type'] == 0]
display(g)

boundary_nodes_list = get_boundary(g)
internal_nodes_list = list(set(g.nodes()) - set(boundary_nodes_list))

unsatisfied_nodes_list = get_unsatisfied_nodes_list(g, internal_nodes_list,
													boundary_nodes_list)


# Loop to move unsatisfied nodes
# vary the value of for loop to visualize different results
for i in range(10000):
	unsatisfied_nodes_list = get_unsatisfied_nodes_list(g, internal_nodes_list,
														boundary_nodes_list)

	make_a_node_satisfied(unsatisfied_nodes_list, empty_cells)

	type1_node_list = [ni for (ni, d) in g.nodes(data=True) if d['type'] == 1]
	type2_node_list = [ni for (ni, d) in g.nodes(data=True) if d['type'] == 2]
	empty_cells = [ni for (ni, d) in g.nodes(data=True) if d['type'] == 0]

display(g)

import networkx as nx

G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (1, 4), (3, 4), (4, 5)])
e = list(G.edges())

def triadic(e):
	new_edges = []


	for i in e:
		a, b = i

		for j in e:
			x, y = j


			if i != j:
				if a == x and (b, y) not in e and (y, b) not in e:
					new_edges.append((b, y))

				if a == y and (b, x) not in e and (x, b) not in e:
					new_edges.append((b, x))

				if b == x and (a, y) not in e and (y, a) not in e:
					new_edges.append((a, y))

				if b == y and (a, x) not in e and (x, a) not in e:

					new_edges.append((a, x))

	return new_edges

print("The possible new edges according to Triadic closure are :")
print(triadic(e))

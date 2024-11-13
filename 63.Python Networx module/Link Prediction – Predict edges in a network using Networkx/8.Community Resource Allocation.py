import networkx as nx

G = nx.Graph()

G.add_node('A', community = 0)
G.add_node('B', community = 0)
G.add_node('C', community = 0)
G.add_node('D', community = 0)
G.add_node('E', community = 1)
G.add_node('F', community = 1)
G.add_node('G', community = 1)
G.add_node('H', community = 1)
G.add_node('I', community = 1)

G.add_edges_from([('A', 'B'), ('A', 'D'), ('A', 'E'), ('B', 'C'),
				('C', 'D'), ('C', 'F'), ('E', 'F'), ('E', 'G'),
							('F', 'G'), ('G', 'H'), ('G', 'I')])

print(list(nx.ra_index_soundarajan_hopcroft(G)))

import osmnx as ox

# load thiruvananthapuram city
place = "Thiruvananthapuram, Kerala"
G = ox.graph_from_place(place, network_type="drive")

# calulate edge length
edge_length = ox.stats.edge_length_total(G)
print("Edge Length:", edge_length)

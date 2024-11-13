import osmnx as ox

place = "Thiruvananthapuram, Kerala"
G = ox.graph_from_place(place, network_type="drive")

# orgin node and destination node
orig, dest = 1141007999, 9992653265

# find shortest path
route_nodes = ox.routing.shortest_path(G, orig, dest, weight="length")

# plot the shortes path
fig, ax = ox.plot_graph_route(G, route_nodes, route_color="r",
                              route_linewidth=6, node_size=0)

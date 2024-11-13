import osmnx as ox

place = "Piedmont, California, USA"
G = ox.graph_from_place(place, network_type="drive")

# find the shortest path (by distance)
# between these nodes then plot it
orig = list(G)[0]
dest = list(G)[140]

# find k-shortest path
routes = ox.k_shortest_paths(G, orig, dest, k=30, weight="length")
fig, ax = ox.plot_graph_routes(
    G, list(routes), route_colors="y",
    route_linewidth=4, node_size=0)

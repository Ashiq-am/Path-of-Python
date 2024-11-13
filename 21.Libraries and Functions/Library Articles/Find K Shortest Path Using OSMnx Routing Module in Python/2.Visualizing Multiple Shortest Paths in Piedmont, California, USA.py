import osmnx as ox


def generate_multindex(route_nodes):
    multiindex_list = []
    # append the index to list
    for u, v in zip(route_nodes[:-1], route_nodes[1:]):
        multiindex_list.append((u, v, 0))
    return multiindex_list


# load the map data
place = "Piedmont, California, USA"
G = ox.graph_from_place(place, network_type="drive")

# find the shortest path (by distance)
# between these nodes then plot it
orig = list(G)[0]
dest = list(G)[140]

# fetch k shortest path
routes_nodes = ox.k_shortest_paths(G, orig, dest, k=30, weight="length")

# get edges from from above multidigraph
gdf_nodes, gdf_edges = ox.graph_to_gdfs(G)

# generate multiindex based on generated shortest route
routes_index_list = []
for route_nodes in routes_nodes:
    multiindex_list = generate_multindex(route_nodes)
    routes_index_list.extend(multiindex_list)

# fetch edge details based on multi index list
shrt_gdf_edges = gdf_edges[gdf_edges.index.isin(routes_index_list)]
# plot the shortest route on map
shrt_gdf_edges.explore(color="red")

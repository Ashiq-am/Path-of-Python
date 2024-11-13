# convert multidigraph nodes to geodataframe
gdf_nodes = ox.utils_graph.graph_to_gdfs(
    multi_digraph, nodes=True, edges=False, node_geometry=True,
    fill_edge_geometry=False)

# display it on map
gdf_nodes.explore()

# convert the edges of multidigrah to geodataframe
geodf_edge = ox.utils_graph.graph_to_gdfs(
    mdigr_bearing, nodes=False, edges=True,
    node_geometry=False, fill_edge_geometry=True)

# plot in map
geodf_edge.explore()

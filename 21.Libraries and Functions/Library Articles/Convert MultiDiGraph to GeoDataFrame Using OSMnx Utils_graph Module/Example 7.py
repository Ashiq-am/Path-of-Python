# convert edges to geodataframe
geodf_edge = ox.utils_graph.graph_to_gdfs(
    multi_digraph, nodes=False, edges=True, node_geometry=False,
    fill_edge_geometry=True)

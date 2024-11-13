# fetch nodes with geometry
geo_dataframe_node = ox.utils_graph.graph_to_gdfs(
    multi_digraph, nodes=True, edges=False, node_geometry=True,
    fill_edge_geometry=False)

# print in jupyter notebook
geo_dataframe_node

import osmnx as ox

# fetch nodes and edges as geodataframe

geo_dataframe = ox.utils_graph.graph_to_gdfs(
    multi_digraph, nodes=True, edges=True,
    node_geometry=False, fill_edge_geometry=False)

# print geodataframe in notebook
geo_dataframe

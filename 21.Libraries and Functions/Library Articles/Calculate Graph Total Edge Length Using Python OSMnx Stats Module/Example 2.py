# convert multidigraph to geodataframe
gdf_nodes, gdf_edges = ox.utils_graph.graph_to_gdfs(G)
gdf_edges['length']

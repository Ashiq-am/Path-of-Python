import osmnx as ox

# set crs attribute
graph_attrs = {"crs": "EPSG:4326"}

# convert geodataframe to multidigraph
multi_digraph = ox.utils_graph.graph_from_gdfs(
    node_gdf, edge_gdf, graph_attrs=graph_attrs)

print(multi_digraph)
multi_digraph.nodes
multi_digraph.edges

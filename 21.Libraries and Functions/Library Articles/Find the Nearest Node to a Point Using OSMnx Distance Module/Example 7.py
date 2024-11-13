import osmnx as ox
import geopandas as gpd

# convert multidigraph nodes to geodataframe
gdf_nodes = ox.utils_graph.graph_to_gdfs(
    multi_digraph, nodes=True, edges=False,
    node_geometry=True, fill_edge_geometry=False)

# convert multidigraph edges to geodataframe
gdf_edges = ox.utils_graph.graph_to_gdfs(
    multi_digraph, nodes=False, edges=True,
    node_geometry=False, fill_edge_geometry=True)

# convert geodataframe nodes to projected gdf noded
gdf_nodes['geometry'] = gdf_nodes.geometry.to_crs("EPSG:7781")
# let's change the x and y columns with projected geometry coordinates
gdf_nodes['x'] = gdf_nodes['geometry'].x
gdf_nodes['y'] = gdf_nodes['geometry'].y

# convert geodataframe edges to projected gdf edges
gdf_edges['geometry'] = gdf_edges.geometry.to_crs("EPSG:7781")

# set crs attribute
graph_attrs = {"crs": "EPSG:7781"}

# convert projected geodataframe to multidigraph
proj_multidigraph = ox.utils_graph.graph_from_gdfs(
    gdf_nodes, gdf_edges, graph_attrs=graph_attrs)

# check for projection
crs = proj_multidigraph.graph["crs"]
gpd.GeoSeries(crs=crs).crs.is_projected

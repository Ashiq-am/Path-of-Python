# get the nearest node id
nearest_nodeid = nearest_node[0]
# create a dictionary with Kokad point and Nearest node coordinates
nearest_node_dict = {'col1': ['Kokad', 'Nearest Node'],
                     'geometry': [Point(kokad_proj_lon, kokad_proj_lat),
                                  LineString([
                                      Point(gdf_nodes.loc[nearest_nodeid].x,
                                            gdf_nodes.loc[nearest_nodeid].y),
                                      Point(kokad_proj_lon, kokad_proj_lat)])]}
# convert to geodataframe
nearest_node_gdf = gpd.GeoDataFrame(nearest_node_dict, crs="EPSG:7781")

# get nearest node map and display it with our dataset
nearest_node_map = nearest_node_gdf.explore(color="red")
gdf_nodes.explore(m=nearest_node_map)

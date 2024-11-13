# find the nearest node from kokad
nearest_node = ox.distance.nearest_nodes(
    proj_multidigraph, kokad_proj_lon, kokad_proj_lat,
    return_dist=True)

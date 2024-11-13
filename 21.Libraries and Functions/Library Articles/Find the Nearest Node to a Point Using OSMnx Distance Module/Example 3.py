# chadayamangalam coordinates
chadaya_lat, chadaya_lon = 8.873103284974913, 76.86933422158793
nearest_node = ox.distance.nearest_nodes(multi_digraph,
                                         chadaya_lon, chadaya_lat,
                                         return_dist=True)

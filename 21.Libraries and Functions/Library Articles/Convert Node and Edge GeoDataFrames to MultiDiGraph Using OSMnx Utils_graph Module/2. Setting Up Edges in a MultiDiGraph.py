# set the edge for multidigraph
edge_dict = {'u': [955820326, 281828280],
             'v': [281828280, 7351760776],
             'key': [0, 0]}
# convert edge dict to geodataframe
edge_gdf = gd.GeoDataFrame(edge_dict, crs=None)
# set multi index
edge_gdf = edge_gdf.set_index(['u', 'v', 'key'])

print(edge_gdf)

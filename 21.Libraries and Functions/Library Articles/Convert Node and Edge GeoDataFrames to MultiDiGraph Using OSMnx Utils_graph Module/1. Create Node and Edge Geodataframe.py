import geopandas as gd

# Coordinates
tvm_lat, tvm_lon = 8.50606, 76.96153
kol_lat, kol_lon = 8.88795, 76.59550
pat_lat, pat_lon = 9.2648, 76.7870

# set the node dictionary for multidigraph
node_dict = {'osmid': [955820326, 281828280, 7351760776],
             'x': [tvm_lon, kol_lon, pat_lon],
             'y': [tvm_lat, kol_lat, pat_lat]
             }
# convert node dictionary to GeoDataFrame
node_gdf = gd.GeoDataFrame(node_dict)

# set osmid as index
node_gdf = node_gdf.set_index('osmid')
print(node_gdf)

import osmnx as ox

# add edge bearing
mdigr_bearing = ox.bearing.add_edge_bearings(G, precision=None)
# get added bearing for edges
mdigr_bearing.edges(data="bearing")

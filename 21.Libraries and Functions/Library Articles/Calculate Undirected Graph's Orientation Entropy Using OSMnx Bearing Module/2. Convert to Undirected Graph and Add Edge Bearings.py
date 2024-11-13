# convert directed to undirected graph
chicago_undirected_graph = ox.utils_graph.get_undirected(chicago_mdigraph)

# add edge bearing
chicago_mdigr_bearing = ox.bearing.add_edge_bearings(
    chicago_undirected_graph, precision=None)

# get bearing
ch_bearings = chicago_mdigr_bearing.edges(data="bearing")

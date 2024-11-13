import osmnx as ox

# fetch data
chn_mdigraph = ox.graph_from_place('Chongqing, China',
                                   network_type="drive")
# convert to undirected graph
chn_mdigraph_undirected = ox.utils_graph.get_undirected(chn_mdigraph)

#calculate average circuity
ox.stats.circuity_avg(chn_mdigraph_undirected)

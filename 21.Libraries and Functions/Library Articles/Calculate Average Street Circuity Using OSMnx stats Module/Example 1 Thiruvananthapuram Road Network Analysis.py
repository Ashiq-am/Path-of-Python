import osmnx as ox

# fetch thiruvananthapuram drive data
tvm_multi_digraph = ox.graph_from_place(
  'Thiruvananthapuram, Kerala', network_type="drive")

# convert it into undirected graph
tvm_mdigraph_undirected = ox.utils_graph.get_undirected(tvm_multi_digraph)

# calculate average circuity
ox.stats.circuity_avg(tvm_mdigraph_undirected)

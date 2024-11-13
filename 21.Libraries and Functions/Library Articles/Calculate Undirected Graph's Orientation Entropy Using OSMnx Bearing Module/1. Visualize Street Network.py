import osmnx as ox

# plot chicago
chicago_mdigraph = ox.graph_from_place('Chicago')
ox.plot_graph(chicago_mdigraph)

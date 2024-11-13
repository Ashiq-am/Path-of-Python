import networkx as nx

# set multidigraph
G = nx.MultiDiGraph(crs="EPSG:4326")

# add each node based on osmid
tvm_osmid, kol_osmid, pat_osmid = 955820326, 281828280, 7351760776
G.add_nodes_from([tvm_osmid, kol_osmid, pat_osmid])

# add coordinates for each node
tvm_lat, tvm_lon = 8.50606, 76.96153
kol_lat, kol_lon = 8.88795, 76.59550
pat_lat, pat_lon = 9.2648, 76.7870
G.nodes[tvm_osmid].update({'osmid': tvm_osmid, 'x': tvm_lon, 'y': tvm_lat})
G.nodes[kol_osmid].update({'osmid': kol_osmid, 'x': kol_lon, 'y': kol_lat})
G.nodes[pat_osmid].update({'osmid': pat_osmid, 'x': pat_lon, 'y': pat_lat})

# add edges
G.add_edges_from([(tvm_osmid, kol_osmid), (kol_osmid, pat_osmid)])

# print nodes
G.nodes
# print edges
G.edges

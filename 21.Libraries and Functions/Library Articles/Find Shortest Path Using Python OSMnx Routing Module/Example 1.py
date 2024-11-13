import osmnx as ox

# load thiruvananthapuram city
place = "Thiruvananthapuram, Kerala"
G = ox.graph_from_place(place, network_type="drive")

# kazhakootam coordinates
kzh_lat, kzh_lon = 8.5686, 76.8731
# medical college coordinates
mdcl_lat, mdcl_lon = 8.52202892500963, 76.926448394559

# fetch the nearest node w.r.t coordinates
kzh_node = ox.distance.nearest_nodes(G, kzh_lon, kzh_lat)
mdcl_node = ox.distance.nearest_nodes(G, mdcl_lon, mdcl_lat)

print("Kazhakkottam Node: {kzh_node}, \
Medical College Node: {mdcl_node}".format(
    kzh_node=kzh_node, mdcl_node=mdcl_node))

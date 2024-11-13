import osmnx as ox

# load thiruvananthapuram city
place = "Thiruvananthapuram, Kerala"
G = ox.graph_from_place(place, network_type="drive")

# get crs
crs = G.graph['crs']
print("CRS-", crs)
# find projected or not
result = ox.projection.is_projected(crs)
print("Is Projected-", result)

import osmnx as ox

place = "Thiruvananthapuram, Kerala"
gdf = ox.features.features_from_address(
    place, {'emergency': True}, dist=3000)
print(gdf)

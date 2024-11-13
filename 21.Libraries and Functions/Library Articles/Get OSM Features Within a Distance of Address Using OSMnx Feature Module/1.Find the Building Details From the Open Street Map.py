import osmnx as ox

# get building details from address within 1000 m
place = "SoHo, New York, NY"
gdf = ox.features.features_from_address(
    place, {'building': True}, dist=1000)

# print first 5 building details
gdf.head(5)

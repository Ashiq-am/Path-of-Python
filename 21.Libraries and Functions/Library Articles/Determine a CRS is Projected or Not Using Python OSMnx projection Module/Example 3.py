import osmnx as ox

# crs for kerala
crs = "epsg:7781"

# find projected or not
result = ox.projection.is_projected(crs)
print("Is Projected-", result)

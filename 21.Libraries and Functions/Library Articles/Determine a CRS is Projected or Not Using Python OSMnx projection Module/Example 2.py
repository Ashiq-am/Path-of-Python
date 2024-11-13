import osmnx as ox

# area of use: India
crs = "EPSG:4146"
# find projected or not
result = ox.projection.is_projected(crs)
print("Is Projected-", result)

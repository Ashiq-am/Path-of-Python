import osmnx as ox

# latitude-longitude point
center_point = (33.299896, -111.831638)

# osm tag
tags = {"leisure": "park"}

# retrieve feature from point
gdf = ox.features_from_point(center_point, tags, dist=1000)

# list first 5 rows from geodataframe
gdf.head(5)

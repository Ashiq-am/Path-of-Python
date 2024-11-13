import osmnx as ox

center_point = (33.299896, -111.831638)
tags = {"leisure": True}

# feature from point
gdf = ox.features_from_point(center_point, tags, dist=1000)

# display it on map
gdf.explore()

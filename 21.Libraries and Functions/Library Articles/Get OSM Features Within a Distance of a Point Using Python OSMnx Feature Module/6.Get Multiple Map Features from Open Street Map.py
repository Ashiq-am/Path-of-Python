import osmnx as ox

# latitude-longitude point
center_point = (33.299896, -111.831638)

# osm tag
tags = {'historic': True,
        'natural': ['grassland', 'tree_row'],
        'landuse': 'religious'}

# retrieve features from point
gdf = ox.features_from_point(center_point, tags, dist=1000)

# display specific columns from geodataframe
gdf[['geometry', 'name', 'historic', 'landuse', 'religion', 'natural']]

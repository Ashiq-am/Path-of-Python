import osmnx as ox

tags = {'amenity': True,
        'landuse': ['retail', 'commercial'],
        'highway': 'bus_stop'}
# fetch multiple features
gdf = ox.features.features_from_address(
    "Thiruvananthapuram, Kerala", tags, dist=500)
# display it on map
gdf.explore()

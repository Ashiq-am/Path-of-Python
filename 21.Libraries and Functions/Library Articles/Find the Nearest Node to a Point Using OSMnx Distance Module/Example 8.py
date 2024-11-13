import geopandas as gpd
from shapely import Point

# set geodataframe
kokad_lat, kokad_lon = 8.984569551375083, 76.87386194013466
kokad_node_dict = {'col1': ['Kokad'],
                   'geometry': [Point(kokad_lon, kokad_lat)]}
kokad_node_gdf = gpd.GeoDataFrame(kokad_node_dict, crs="EPSG:4326")

# convert it to projected coordinates
kokad_node_gdf['geometry'] = kokad_node_gdf.geometry.to_crs("EPSG:7781")

# get projected coordinates
kokad_proj_lon = kokad_node_gdf['geometry'].x
kokad_proj_lat = kokad_node_gdf['geometry'].y

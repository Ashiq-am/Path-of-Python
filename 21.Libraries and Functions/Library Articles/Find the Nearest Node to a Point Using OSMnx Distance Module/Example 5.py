import geopandas as gpd
from shapely import (
    Point, LineString)

# create a new geodataframe with the nearest node and new point
nearest_node_dict = {'col1': ['Chadayamangalam', 'Nearest Node'],
                     'geometry': [Point(chadaya_lon, chadaya_lat),
                                  LineString([
                                      Point(gdf_nodes.loc[nearest_nodeid].x,
                                            gdf_nodes.loc[nearest_nodeid].y),
                                      Point(chadaya_lon, chadaya_lat)])]}
# convert dictionary to geodataframe
nearest_node_gdf = gpd.GeoDataFrame(nearest_node_dict, crs="EPSG:4326")
# nearest node map reference
nearest_node_map = nearest_node_gdf.explore(color="red")
# combine nearest node with existing node map
gdf_nodes.explore(m=nearest_node_map)

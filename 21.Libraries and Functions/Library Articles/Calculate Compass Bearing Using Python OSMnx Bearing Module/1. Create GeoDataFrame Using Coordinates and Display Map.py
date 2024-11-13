import geopandas as gd
from shapely.geometry import Point

# coordinates
tvm_lat, tvm_lon = 8.50606, 76.96153
kol_lat, kol_lon = 8.88795, 76.59550
coordinate_dict = {'name': ['Thiruvananthapuram', 'Kollam'],
                   'geometry': [Point(tvm_lon, tvm_lat),
                                Point(kol_lon, kol_lat)]}
# convert corrdinate dictionary to geo dataframe
gdf = gd.GeoDataFrame(coordinate_dict, crs="EPSG:4326")
# displays the map in jupyter
gdf.explore()

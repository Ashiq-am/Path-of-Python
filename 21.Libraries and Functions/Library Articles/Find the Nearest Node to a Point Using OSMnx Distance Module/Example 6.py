import geopandas as gpd
import osmnx as ox

# fecth multi digraph from place
multi_digraph = ox.graph_from_place('Punalur, Kerala')

# fetch the crs from multidigraph
crs = multi_digraph.graph["crs"]

# check whether the crs is projected
gpd.GeoSeries(crs=crs).crs.is_projected

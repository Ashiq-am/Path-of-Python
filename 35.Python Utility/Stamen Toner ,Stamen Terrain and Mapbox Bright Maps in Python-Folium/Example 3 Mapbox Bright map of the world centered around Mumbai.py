import numpy as np
import pandas as pd
import folium

# define the world map
world_map = folium.Map()

# create a Mapbox Bright map of the world
# centered around Mumbai with a zoom level
# of 10
world_map = folium.Map(location =[19.11763765873, 72.9060384756],
					zoom_start = 10, tiles ='Mapbox Bright')

# display the map
world_map

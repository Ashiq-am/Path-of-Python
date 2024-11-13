import osmnx as ox
import numpy as np

# coordinates
tvm_lat, tvm_lon = 8.50606, 76.96153
mum_lat, mum_lon = 19.0760, 72.8777
dlh_lat, dlh_lon = 28.6139, 77.2090

# set array of coordinates
from_lat = np.array([tvm_lat, dlh_lat])
from_lon = np.array([tvm_lon, dlh_lon])
to_lat = np.array([mum_lat, tvm_lat])
to_lon = np.array([mum_lon, tvm_lon])

# great circle distance for array of params
ox.distance.great_circle(
    from_lat, from_lon, to_lat, to_lon,
    earth_radius=6371009)

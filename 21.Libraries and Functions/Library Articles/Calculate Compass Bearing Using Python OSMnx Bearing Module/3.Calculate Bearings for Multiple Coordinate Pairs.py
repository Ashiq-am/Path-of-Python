import osmnx as ox
import numpy as np

# Thiruvananthapuram coordinates
tvm_lat, tvm_lon = 8.50606, 76.96153
# Kollam coordinates
kol_lat, kol_lon = 8.88795, 76.59550
# Pathanamthitta coordinates
pat_lat, pat_lon = 9.2648, 76.7870

# Calculate bearing for (trivandrum, kollam)
# and (kollam , pathanamthitta)
from_lat = np.array([tvm_lat, kol_lat])
from_lon = np.array([tvm_lon, kol_lon])
to_lat = np.array([kol_lat, pat_lat])
to_lon = np.array([kol_lon, pat_lon])
# calculate bearing
bearing = ox.bearing.calculate_bearing(from_lat, from_lon, to_lat, to_lon)
bearing

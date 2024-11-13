import osmnx as ox
# coordinates
tvm_lat, tvm_lon = 8.50606, 76.96153
nwdelhi_lat, nwdelhi_lon = 28.6139, 77.2090

# great circle distance
ox.distance.great_circle(
    nwdelhi_lat, nwdelhi_lon, tvm_lat, tvm_lon,
    earth_radius=6371009)

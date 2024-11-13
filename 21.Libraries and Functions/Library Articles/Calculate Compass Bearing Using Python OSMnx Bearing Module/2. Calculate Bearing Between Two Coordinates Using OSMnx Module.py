import osmnx as ox
# coordinates
tvm_lat, tvm_lon = 8.50606, 76.96153
kol_lat, kol_lon = 8.88795, 76.59550
# calculate bearing
bearing = ox.bearing.calculate_bearing(tvm_lat, tvm_lon, kol_lat,  kol_lon)
bearing

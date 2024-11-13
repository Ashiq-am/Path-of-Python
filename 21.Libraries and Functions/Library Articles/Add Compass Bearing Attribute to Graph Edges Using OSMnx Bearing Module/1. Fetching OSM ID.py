from geopy.geocoders import Nominatim

# Thiruvananthapuram Coordinates
tvm_lat, tvm_lon = 8.50606, 76.96153

# Nominatim for reverse geolocator
geolocator = Nominatim(user_agent="sample_app")
tvm_osmid = "{lat}, {lon}".format(lat=tvm_lat, lon=tvm_lon)
location = geolocator.reverse(tvm_osmid)

# fetch osm id
location.raw.get('osm_id')

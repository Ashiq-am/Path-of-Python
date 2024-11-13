from geopy.geocoders import Nominatim
# fetch osm id
geolocator = Nominatim(user_agent="sample_app")
tvm_osmid = "{lat}, {lon}".format(lat=tvm_lat, lon=tvm_lon)
location = geolocator.reverse(tvm_osmid)
location.raw.get('osm_id')

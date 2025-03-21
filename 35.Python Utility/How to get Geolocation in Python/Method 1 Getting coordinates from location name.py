# importing geopy library
from geopy.geocoders import Nominatim

# calling the Nominatim tool
loc = Nominatim(user_agent="GetLoc")

# entering the location name
getLoc = loc.geocode("Gosainganj Lucknow")

# printing address
print(getLoc.address)

# printing latitude and longitude
print("Latitude = ", location.latitude, "\n")
print("Longitude = ", location.longitude)

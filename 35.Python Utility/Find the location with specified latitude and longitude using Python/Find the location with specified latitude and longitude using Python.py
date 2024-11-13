# Import module
from geopy.geocoders import Nominatim

# Initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")

# Assign Latitude & Longitude
Latitude = "25.594095"
Longitude = "85.137566"

# Dsiaplying Latitude and Longitude
print("Latitude: ", Latitude)
print("Longitude: ", Longitude)

# Get location with geocode
location = geolocator.geocode(Latitude+","+Longitude)

# Dsiplay location
print("\nLocation of the given Latitude and Longitude:")
print(location)

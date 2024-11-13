# Importing the great_circle module from the library
from geopy.distance import great_circle

# Loading the lat-long data for Kolkata & Delhi
kolkata = (22.5726, 88.3639)
delhi = (28.7041, 77.1025)

# Print the distance calculated in km
print(great_circle(kolkata, delhi).km)

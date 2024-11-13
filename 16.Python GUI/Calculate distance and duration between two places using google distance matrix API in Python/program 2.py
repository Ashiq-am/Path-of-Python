# importing googlemaps module
import googlemaps

# Requires API key
gmaps = googlemaps.Client(key='Your_API_key')

# Requires cities name
my_dist = gmaps.distance_matrix('Delhi','Mumbai')['rows'][0]['elements'][0]

# Printing the result
print(my_dist)

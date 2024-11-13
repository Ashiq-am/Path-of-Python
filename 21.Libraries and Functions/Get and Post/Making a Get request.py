# importing the requests library
import requests

# api-endpoint
URL = "http://maps.googleapis.com/maps/api/geocode/json"

# location given here
location = "delhi technological university"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'address':location}

# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)

# extracting data in json format
data = r.json()


# extracting latitude, longitude and formatted address
# of the first matching location
latitude = data['results'][0]['geometry']['location']['lat']
longitude = data['results'][0]['geometry']['location']['lng']
formatted_address = data['results'][0]['formatted_address']

# printing the output
print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
	%(latitude, longitude,formatted_address))















'''The above example finds latitude, longitude and formatted address of a given location by sending a GET 
request to the Google Maps API. 
An API (Application Programming Interface) enables you to access the internal features of a program in a 
limited fashion. 

And in most cases, the data provided is in JSON(JavaScript Object Notation) format 
(which is implemented as dictionary objects in Python!).'''
# Python program to find live hotel prices
# Python program to find live hotel prices
# status using Makcorps Hotel API

# import required modules
import requests, json

# base_url variable to store url
base_url = "https://api.makcorps.com/free/"

# enter city name here
city = "london"

# complete_url variable to
# store complete url address
complete_url = base_url + city

# Declaring headers needed
headers = {
	'Authorization': 'JWT your_API_id',
}

# get method of requests module
# return response object
response_ob = requests.get(complete_url, headers=headers)

# json method of response object convert
# json format data into python format data
result = response_ob.json()

# Now check the value of status_code is equal
# to "200" or not, if equal that means record is
# found otherwise record is not found
if response_ob.status_code == 200:

	# name is extracting from
	# the result variable data
	print("price comparison data for a random date of city london is:")
	print(result)
else:
	print("record is not found for given request")

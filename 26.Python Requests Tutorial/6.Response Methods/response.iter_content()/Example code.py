# import requests module
import requests

# Making a get request
response = requests.get('https://geeksforgeeks.org')

# print response
print(response)

# print iter_content data
print(response.iter_content())

# iterates over the list
for i in response.iter_content():
	print(i)

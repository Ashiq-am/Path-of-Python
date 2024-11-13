# import requests module
import requests

# Making a get request
response = requests.get('https://geeksforgeeks.org')

# print response
print(response)

# print is_redirect Flag
print(response.is_redirect)

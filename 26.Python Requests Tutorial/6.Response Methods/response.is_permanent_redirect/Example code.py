# import requests module
import requests

# Making a get request
response = requests.get('https://geeksforgeeks.org')

# print response
print(response)

# print is_permanent_redirect flag
print(response.is_permanent_redirect)

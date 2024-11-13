# import requests module
import requests

# Making a get request
response = requests.get('https://api.github.com/')

# print response
print(response)

# print check if an error has occurred
print(response.raise_for_status())

# ping an incorrect url
response = requests.get('https://geeksforgeeks.org / naveen/')

# print check if an error has occurred
print(response.raise_for_status())

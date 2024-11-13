# import requests module
import requests

# Making a get request
response = requests.get('https://api.github.com/')

# print response
print(response)

# print the reason
print(response.reason)

# ping an incorrect url
response = requests.get('https://geeksforgeeks.org / naveen/')

# print response
print(response)

# print the reason now
print(response.reason)

# import requests module
import requests

# Making a get request
response = requests.get('https://github.com', verify ='/path / to / certfile')

# print request object
print(response)

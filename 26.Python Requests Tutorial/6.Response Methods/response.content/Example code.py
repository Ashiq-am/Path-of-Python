import requests

# Making a get request
response = requests.get('https://api.github.com')

# prinitng request content
print(response.content)

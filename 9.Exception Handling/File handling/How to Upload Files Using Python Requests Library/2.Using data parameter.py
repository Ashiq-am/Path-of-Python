import requests

url = 'https://httpbin.org/post'
data = {'key': 'value'}  # Additional data if required

with open('file.txt', 'rb') as file:
    response = requests.post(url, data=data, files={'file': file})

print(response.text)

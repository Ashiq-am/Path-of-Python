import requests

url = 'https://httpbin.org/post'
# Specify the content type
headers = {'Content-Type': 'application/octet-stream'}
data = open('file.txt', 'rb').read()

response = requests.post(url, headers=headers, data=data)

print(response.text)

import requests

url = 'https://httpbin.org/post'
files = {'file': ('example.txt', open('example.txt', 'rb'),
                  'multipart/form-data')}

response = requests.post(url, files=files)

print(response.text)

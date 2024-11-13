import requests

url = "https://httpbin.org/post"

data = {
	"id": 1001,
	"name": "geek",
	"passion": "coding",
}

response = requests.post(url, data=data)

print("Status Code", response.status_code)
print("JSON Response ", response.json())

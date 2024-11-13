import requests
import json

url = "https://httpbin.org/post"

headers = {"Content-Type": "application/json; charset=utf-8"}

data = {
	"id": 1001,
	"name": "geek",
	"passion": "coding",
}

jsonObject = json.dumps(data)
response = requests.post(url, headers=headers, json=jsonObject)

print("Status Code", response.status_code)
print("JSON Response ", response.json())

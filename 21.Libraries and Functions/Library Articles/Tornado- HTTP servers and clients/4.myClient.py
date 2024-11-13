import requests

url = "http://localhost:8003"

data = {
    "name": "Abul Hasan",
    "email": "abulhax@gmail.com"
}

response = requests.post(url, data=data)

print(response.text)

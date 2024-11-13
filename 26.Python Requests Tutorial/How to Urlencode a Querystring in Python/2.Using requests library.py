import requests
data = {
    "site": "GeeksforGeeks",
    "topic": "Python URL encoding",
    "level": "Intermediate"
}
encoded_data = requests.models.RequestEncodingMixin._encode_params(data)
print(encoded_data)

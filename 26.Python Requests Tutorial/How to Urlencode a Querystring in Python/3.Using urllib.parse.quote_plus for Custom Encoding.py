import urllib.parse
data = {
    "site": "GeeksforGeeks",
    "topic": "Python URL encoding",
    "level": "Intermediate"
}
encoded_data = '&'.join([f"{urllib.parse.quote_plus(key)}={urllib.parse.quote_plus(value)}" for key, value in data.items()])
print(encoded_data)

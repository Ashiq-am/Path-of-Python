import urllib.parse
data = {
    "site": "GeeksforGeeks",
    "topic": "Python URL encoding",
    "level": "Intermediate"
}
encoded_data = urllib.parse.urlencode(data)
print(encoded_data)

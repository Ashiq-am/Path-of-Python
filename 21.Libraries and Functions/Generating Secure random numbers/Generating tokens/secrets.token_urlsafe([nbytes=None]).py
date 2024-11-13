import secrets

url = 'https://mydomain.com/reset=' + secrets.token_urlsafe()
print(url)

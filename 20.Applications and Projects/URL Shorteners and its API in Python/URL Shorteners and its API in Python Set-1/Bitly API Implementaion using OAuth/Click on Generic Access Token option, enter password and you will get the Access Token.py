import bitly_api

BITLY_ACCESS_TOKEN ="ACCESS_TOKEN"

b = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN)

response = b.shorten('http://google.com/')
print(response)

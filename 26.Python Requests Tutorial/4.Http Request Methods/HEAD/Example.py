import requests

# Making a HEAD request
r = requests.head('https://httpbin.org/', data ={'key':'value'})

# check status code for response recieved
# success code - 200
print(r)

# print headers of request
print(r.headers)

# checking if request contains any content
print(r.content)

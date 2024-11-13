import requests

# Making a PATCH request
r = requests.patch('https://httpbin.org / patch', data ={'key':'value'})

# check status code for response recieved
# success code - 200
print(r)

# print content of request
print(r.content)

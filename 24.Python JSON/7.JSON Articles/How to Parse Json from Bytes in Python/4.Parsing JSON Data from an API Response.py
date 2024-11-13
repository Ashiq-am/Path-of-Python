import json
import urllib.request

# Make a request to an API endpoint
url = 'https://jsonplaceholder.typicode.com/posts/1'
response = urllib.request.urlopen(url)

# Get the JSON data from the response
json_data_api = response.read()

# Decode bytes to string and parse JSON
decoded_data_api = json_data_api.decode('utf-8')
parsed_json_api = json.loads(decoded_data_api)

# Accessing values from parsed JSON
user_id = parsed_json_api['userId']
title = parsed_json_api['title']
body = parsed_json_api['body']

# Printing parsed values
print("User ID:", user_id)
print("Title:", title)
print("Body:", body)

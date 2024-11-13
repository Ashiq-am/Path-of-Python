import json
import requests

# Get dummy data using an API
res = requests.get("http://dummy.restapiexample.com/api/v1/employees")

# Convert data to dict
data = json.loads(res.text)

# Convert dict to string
data = json.dumps(data)

print(data)
print(type(data))

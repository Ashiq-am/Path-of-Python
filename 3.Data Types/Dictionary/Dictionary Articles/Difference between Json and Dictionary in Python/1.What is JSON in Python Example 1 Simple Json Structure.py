import json

# some JSON:
a = '{ "name":"Rahul", "age":21, "city":"Banglore"}'
# parse x:

b = json.loads(a)
print(b["city"])

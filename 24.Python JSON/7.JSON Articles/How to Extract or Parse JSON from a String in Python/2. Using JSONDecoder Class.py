import json

s = '{"one" : "1", "two" : "2", "three" : "3"}'

decoder = json.JSONDecoder()

data = decoder.decode(s)
print(data)

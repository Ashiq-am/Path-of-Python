import json
# 5 is in string type
json_data = '{ "numbers": [1, 2, 3, 4, "5"] }'

data = json.loads(json_data)
numbers = data["numbers"]
try:
	total = sum(numbers)
	print(total)
except TypeError:
	print("Mismatch Type Detected")

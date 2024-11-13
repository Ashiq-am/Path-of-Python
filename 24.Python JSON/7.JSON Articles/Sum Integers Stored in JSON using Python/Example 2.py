import json

def sumIntegers(jsonFile, attribute):
	with open(jsonFile, 'r') as file:
		data = json.load(file)

	sum = 0
	for item in data:
		if attribute in item and isinstance(item[attribute], int):
			sum += item[attribute]

	return sum

# Create a file.json with a list of items
with open('file.json', 'w') as json_file:
	json.dump([
		{"name": "Item1", "value": 10},
		{"name": "Item2", "value": 5},
		{"name": "Item3", "value": "NotAnInteger"},
		{"name": "Item4", "value": 7}
	], json_file)

# Call the function with the created file and attribute
result = sumIntegers('file.json', 'value')

# Print the result
print(f"The sum of integers in the 'value' attribute of JSON file is: {result}")

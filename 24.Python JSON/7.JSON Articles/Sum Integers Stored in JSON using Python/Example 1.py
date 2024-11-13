import json

def sumOfInt(jsonFile):
	with open(jsonFile, 'r') as file:
		data = json.load(file)
	sum = 0
	for key, val in data.items():
		if isinstance(val, int):
			sum += val
	return sum

# Create a file.json with sample data
with open('file.json', 'w') as json_file:
	json.dump({"number1": 10, "number2": 5, "text": "Hello", "number3": 7, "number4": 3}, json_file)

# Call the function with the created file
result = sumOfInt('file.json')

# Print the result
print(f"The sum of integers in the JSON file is: {result}")

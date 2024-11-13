import json

# Dictionary to serve as a cache for file contents, preventing redundant file reads
file_cache = {}

def read_file_json(file_path):
	# Check if file content is already in the cache
	if file_path not in file_cache:
		# Open the file in read mode
		with open(file_path, 'r') as file:
			# Load the JSON content from the file
			file_content = json.load(file)

			# Cache the file content for future use
			file_cache[file_path] = file_content

	# Return the file content either from the cache or newly loaded
	return file_cache[file_path]

# Example Usage
# Create a sample JSON file for demonstration purposes
data = {'website': 'geeksforgeeks'}
with open('example.json', 'w') as file:
	json.dump(data, file)

# Read the content of the JSON file using the read_file_json function
result = read_file_json('example.json')

# Print the result obtained from the file read operation
print(result)

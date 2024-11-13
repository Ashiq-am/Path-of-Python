import functools

@functools.lru_cache(maxsize=2)
def read_file_with_lru_cache(file_path):
	"""
	Function to read the content of a file with function-level caching using LRU Cache.

	Parameters:
	- file_path (str): The path of the file to be read.

	Returns:
	- str: The content of the file.
	"""
	# Read the file content
	with open(file_path, 'r') as file:
		file_content = file.read()
		print(f"Reading from file: {file_path}")

	return file_content

result1 = read_file_with_lru_cache('example.txt')
result2 = read_file_with_lru_cache('example.txt')

# Displaying the results
print("Result 1:", result1)
print("Result 2:", result2)

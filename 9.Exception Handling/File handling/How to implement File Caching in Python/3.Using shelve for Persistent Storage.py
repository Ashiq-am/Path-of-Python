import shelve

def read_file_with_cache(file_path):
	# Using a shelve file as a persistent cache
	with shelve.open('file_cache.db') as cache:
		# Check if the file path is already in the cache
		if file_path not in cache:
			# If not in the cache, read the file and store its content in the cache
			with open(file_path, 'r') as file:
				file_content = file.read()
				cache[file_path] = file_content
				print(f"Reading from file: {file_path}")
		else:
			# If in the cache, retrieve the content from the cache
			print(f"Reading from cache: {file_path}")

		# Return the content either from the cache or newly read file
		return cache[file_path]

with open('example.txt', 'w') as file:
	file.write("This is some example text.")

# Reading the file using the caching function
result1 = read_file_with_cache('example.txt')
result2 = read_file_with_cache('example.txt')

# Displaying the results
print("Result 1:", result1)
print("Result 2:", result2)

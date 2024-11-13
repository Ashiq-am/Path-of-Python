file_path = "/path/to/nonexistent_file.txt"

try:
	with open(file_path, 'r') as file:
		content = file.read()
	print(content)
except FileNotFoundError as e:
	print(f"FileNotFoundError: {e}")

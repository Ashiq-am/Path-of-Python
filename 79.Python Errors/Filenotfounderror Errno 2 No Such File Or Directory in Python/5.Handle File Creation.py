file_path = "/path/to/nonexistent_file.txt"

try:
	with open(file_path, 'r') as file:
		content = file.read()
	print(content)
except FileNotFoundError:
	print(f"File not found at {file_path}. Creating the file.")
	with open(file_path, 'w') as file:
		file.write("Default content")

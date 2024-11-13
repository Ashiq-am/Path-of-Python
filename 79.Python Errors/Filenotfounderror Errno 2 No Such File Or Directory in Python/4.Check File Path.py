import os

file_path = "/path/to/missing_file.txt"

if os.path.exists(file_path):
	with open(file_path, 'r') as file:
		content = file.read()
	print(content)
else:
	print(f"File not found at {file_path}")

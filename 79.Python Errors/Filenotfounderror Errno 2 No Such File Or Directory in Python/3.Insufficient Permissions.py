file_path = "/restricted_folder/confidential.txt"

try:
	with open(file_path, 'r') as file:
		content = file.read()
	print(content)
except FileNotFoundError as e:
	print(f"FileNotFoundError: {e}")

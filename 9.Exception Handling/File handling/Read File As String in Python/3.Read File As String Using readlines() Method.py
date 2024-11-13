file_path = 'example.txt'

with open(file_path, 'r') as file:
	lines = file.readlines()
	file_content = ''.join(lines)

print(file_content)

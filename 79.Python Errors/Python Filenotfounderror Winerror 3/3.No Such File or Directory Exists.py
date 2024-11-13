try:
	file_path = 'non_existent_file.txt'
	with open(file_path, 'r') as file:
		content = file.read()
	print("File content:", content)
except FileNotFoundError as e:
	print("File not found:", e)
except Exception as e:
	print("An error occurred:", e)

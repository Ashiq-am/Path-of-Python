import encodings
with open('example.txt', 'r', encoding='utf-8') as file:
	content = file.read()
	print(content)

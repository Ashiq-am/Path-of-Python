import re

def approach2Fn(filename, old_lines, new_lines):
	with open(filename, 'r') as file:
		data = file.read()
	for old, new in zip(old_lines, new_lines):
		data = re.sub(re.escape(old), new, data)
	with open(filename, 'w') as file:
		file.write(data)
	res = data.split('\n')
	for line in res:
		print(line)

old_lines = ["Geeks for Geeks", "Python is awesome"]
new_lines = ["GFG", "Python is amazing"]
approach2Fn('input.txt', old_lines, new_lines)

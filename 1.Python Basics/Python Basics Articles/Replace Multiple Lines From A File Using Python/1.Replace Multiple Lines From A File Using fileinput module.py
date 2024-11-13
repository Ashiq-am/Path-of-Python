import fileinput

def approach1Fn(filename, old_lines, new_lines):
	res = []
	with fileinput.FileInput(filename, inplace=True,) as file:
		for line in file:
			for old, new in zip(old_lines, new_lines):
				line = line.replace(old, new)
			res.append(line)
			print(line, end='')

	return res

old_lines = ["Geeks for Geeks", "Python is awesome"]
new_lines = ["GFG", "Python is amazing"]
res = approach1Fn('input.txt', old_lines, new_lines)
for line in res:
	print(line, end='')
with open('input.txt', 'w') as file:
	for line in res:
		file.write(line)

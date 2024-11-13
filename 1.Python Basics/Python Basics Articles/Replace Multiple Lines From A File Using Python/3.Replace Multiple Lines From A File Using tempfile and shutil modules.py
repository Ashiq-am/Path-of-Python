import tempfile
import shutil


def approach2Fn(filename, old_lines, new_lines):
	updated_lines = []
	temp_file = tempfile.NamedTemporaryFile(delete=False)

	with open(filename, 'r') as file:
		for line_number, line in enumerate(file, start=1):
			for old, new in zip(old_lines, new_lines):
				line = line.replace(old, new)
			temp_file.write(line.encode())
			updated_lines.append(line.strip())
	temp_file.close()
	shutil.move(temp_file.name, filename)
	return updated_lines


old_lines = ["Geeks for Geeks", "Python is awesome"]
new_lines = ["GFG", "Python is amazing"]
res = approach2Fn('input.txt', old_lines, new_lines)
for line in res:
	print(line)
with open('input.txt', 'w') as file:
	for line in res:
		file.write(line + '\n')

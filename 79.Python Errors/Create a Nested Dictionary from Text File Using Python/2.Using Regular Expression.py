import re
res = {}
with open('input.txt', 'r') as file:
	for line in file:
		match = re.match(r'\s*([^:]+)\s*:\s*(.+)\s*', line)
		if match:
			key, value = match.groups()
			if ',' in value:
				res[key] = value.split(',')
			else:
				res[key] = value
print(res)

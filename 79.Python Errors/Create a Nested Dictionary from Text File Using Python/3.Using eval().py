res = {}
with open('input.txt', 'r') as file:
	for line in file:
		if ':' in line:
			key, value = line.strip().split(':', 1)
			res[key] = eval(value)
print(res)

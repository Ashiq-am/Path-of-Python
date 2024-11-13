a = open('gfg1.txt', 'r').readlines()
b = open('gfg2.txt', 'r').readlines()
output = []

for item in b:
	if item not in a:
		output.append(item)

with open('resultant.txt', 'w') as res:
	for line in output:
		res.write(line)

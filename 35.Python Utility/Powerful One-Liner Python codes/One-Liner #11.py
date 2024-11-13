file = open('gfg.txt', 'r')
lis =[]

for each in file:

	# removing '\n' from the end of the string
	a = each[:-1]
	lis.append(a)

file.close()

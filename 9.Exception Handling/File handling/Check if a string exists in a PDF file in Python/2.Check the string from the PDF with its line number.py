St = 'suraj'
f = open("file1.pdf", "r")

c = 0
line = 0

for a in f:
	line = line + 1

	if St in a:
		c = 1
		break

if c == 0:
	print('String \'', St, '\' Not Found')
else:
	print('String \'', St, '\' Is Found In Line', line)

f.close()

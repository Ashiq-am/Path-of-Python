St = 'suraj'
f = open("file1.pdf", "r")
a = f.read()

if St in a:
	print('String \'', St, '\' Is Found In The PDF File')
else:
	print('String \'', St, '\' Not Found')

f.close()

# Iterates over the file
f = open(__file__, 'r')

#next()
try:
	while f.next():
		print(f.next())
except:
	f.close()

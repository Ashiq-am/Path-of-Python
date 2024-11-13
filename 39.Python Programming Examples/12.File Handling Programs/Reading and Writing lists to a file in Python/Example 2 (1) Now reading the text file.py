# open file in read mode
f = open('gfg.txt', 'r')

# display content of the file
for x in f.readlines():
	print(x, end='')

# close the file
f.close()

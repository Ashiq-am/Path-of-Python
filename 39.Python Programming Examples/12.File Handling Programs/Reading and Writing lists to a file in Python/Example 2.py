# assign list
l = ['Geeks', '4', 'geeks']

# open file
with open('gfg.txt', 'a') as f:

	# write elements of list
	for items in l:
		f.write('%s\n' % items)

	print("File appended successfully")

# close the file
f.close()

with open('GFG.txt', 'rb') as file1, open('log.txt', 'rb') as file2:
	data1 = file1.read()
	data2 = file2.read()

if data1 != data2:
	print("Files do not match.")
else:
	print("Files match.")

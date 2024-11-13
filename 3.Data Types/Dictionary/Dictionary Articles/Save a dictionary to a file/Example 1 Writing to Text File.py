dictionary = {'geek': 1, 'supergeek': True, 4: 'geeky'}

try:
	geeky_file = open('geekyfile.txt', 'wt')
	geeky_file.write(str(dictionary))
	geeky_file.close()

except:
	print("Unable to write to file")

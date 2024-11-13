dictionary = {'geek': 1, 'supergeek': True, 4: 'geeky'}

try:
	geeky_file = open('geekyfile.txt', 'a')
	geeky_file.write(str(dictionary))
	geeky_file.close()

except:
	print("Unable to append to file")

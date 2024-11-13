import pickle

dictionary = {'geek': 1, 'supergeek': True, 4: 'geeky'}

try:
	geeky_file = open('geekyfile', 'wb')
	pickle.dump(dictionary, geeky_file)
	geeky_file.close()

except:
	print("Something went wrong")

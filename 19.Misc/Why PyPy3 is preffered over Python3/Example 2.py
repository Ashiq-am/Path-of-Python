# No Race condition
File_name ="test.txt"

try:
	f = open(File_name)
except IOError:
	print("No such file accessed")
else:
	with f:
		print(f.read())

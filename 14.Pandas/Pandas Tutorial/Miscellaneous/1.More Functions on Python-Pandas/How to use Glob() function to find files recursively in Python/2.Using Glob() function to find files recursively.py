# Python program to find files
# recursively using Python


import glob


# Returns a list of names in list files.
print("Using glob.glob()")
files = glob.glob('/home/geeks/Desktop/gfg/**/*.txt',
				recursive = True)
for file in files:
	print(file)


# It returns an iterator which will
# be printed simultaneously.
print("\nUsing glob.iglob()")
for filename in glob.iglob('/home/geeks/Desktop/gfg/**/*.txt',
						recursive = True):
	print(filename)

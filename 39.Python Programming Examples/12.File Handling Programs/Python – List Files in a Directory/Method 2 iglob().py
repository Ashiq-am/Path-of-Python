import glob

# This is my path
path="C:\\Users\\Vanshi\\Desktop\\gfg**\\*.txt"



# It returns an iterator which will
# be printed simultaneously.
print("\nUsing glob.iglob()")

# Prints all types of txt files present in a Path
for file in glob.iglob(path, recursive=True):
	print(file)

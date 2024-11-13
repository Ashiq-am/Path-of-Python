import glob

# This is my path
path="C:\\Users\\Vanshi\\Desktop\\gfg"

# Using '*' pattern
print('\nNamed with wildcard *:')
for files in glob.glob(path + '*'):
	print(files)

# Using '?' pattern
print('\nNamed with wildcard ?:')
for files in glob.glob(path + '?.txt'):
	print(files)


# Using [0-9] pattern
print('\nNamed with wildcard ranges:')
for files in glob.glob(path + '/*[0-9].*'):
	print(files)

# Python program to list out
# all the empty directories


import os

# List comprehension to enter
# all empty directories to list

empty = [root for root, dirs, files, in os.walk('Test')
				if not len(dirs) and not len(files)]

print("Empty Directories:")
print(empty)

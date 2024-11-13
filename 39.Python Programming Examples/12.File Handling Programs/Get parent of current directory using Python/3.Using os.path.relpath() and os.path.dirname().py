# Python program to get the
# parent directory


import os.path

# function to get parent
def getParent(path, levels = 1):
	common = path

	# Using for loop for getting
	# starting point required for
	# os.path.relpath()
	for i in range(levels + 1):

		# Starting point
		common = os.path.dirname(common)

	# Parent directory upto specified
	# level
	return os.path.relpath(path, common)

path = 'D:/Pycharm projects / GeeksforGeeks / Nikhil / gfg.txt'
print(getParent(path, 2))

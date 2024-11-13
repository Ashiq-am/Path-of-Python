# Python program to demonstrate
# shutil.copytree()


# Importing module
import shutil
import errno

# Source path
src = 'D:/Pycharm projects/GeeksforGeeks/src/b/test_b.txt'

# Destination path
dest = 'D:/Pycharm projects/GeeksforGeeks/dst'

# Copy the content of
# source to destination
try:
	shutil.copytree(src, dest)
except OSError as err:

	# error caused if the source was not a directory
	if err.errno == errno.ENOTDIR:
		shutil.copy2(src, dest)
	else:
		print("Error: % s" % err)

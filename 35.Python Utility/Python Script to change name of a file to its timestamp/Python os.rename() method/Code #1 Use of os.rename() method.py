# Python program to explain os.rename() method

# importing os module
import os


# Source file path
source = 'GeeksforGeeks/file.txt'

# destination file path
dest = 'GeekforGeeks/newfile.txt'


# Now rename the source path
# to destination path
# using os.rename() method
os.rename(source, dest)
print("Source path renamed to destination path successfully.")

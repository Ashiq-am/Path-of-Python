# Python program to explain os.path.dirname() method

# importing os.path module
import os.path

# Path
path = '/home/User/Documents'

# Get the directory name
# from the specified path
dirname = os.path.dirname(path)

# Print the directory name
print(dirname)

# Path
path = '/home/User/Documents/file.txt'

# Get the directory name
# from the specified path
dirname = os.path.dirname(path)

# Print the directory name
print(dirname)

# Path
path = 'file.txt'

# Get the directory name
# from the specified path
dirname = os.path.dirname(path)

# Print the directory name
print(dirname)

# In the above specified path
# does not contains any
# directory so,
# It will print Nothing
